from tag.models import Tag
from tempfile import NamedTemporaryFile
from django.core.files.base import File
from django.test.testcases import TestCase
from django.test import Client
from rest_framework.utils import json
from recitation.models import Recitation
from freezegun import freeze_time
from django.contrib.auth import get_user_model
from pytest import importorskip

importorskip("random_hello")
HemontikaUser = get_user_model()


@freeze_time("2021-01-01 11:12:13.000000")
class TestViews(TestCase):

    DATE = "2021-01-01T11:12:13Z"

    @classmethod
    def setUpTestData(cls):
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        recite = Recitation(reciter=jack, title="random title", description="random description", language="en")
        temp_audio = File(NamedTemporaryFile(suffix="mp3"))
        temp_image = File(NamedTemporaryFile(suffix="jpg"))
        temp_audio.name = "test_audio.mp3"
        temp_image.name = "test_image.jpg"
        recite.recitation_audio = temp_audio
        recite.thumbnail_pic = temp_image
        recite.save()
        tag1 = Tag.objects.create(name="classics")
        tag2 = Tag.objects.create(name="song")
        tag1.recitation_set.add(recite)
        tag2.recitation_set.add(recite)
        recite = Recitation(reciter=jack, title="random title2", description="random description 2", language="bn")
        temp_audio = File(NamedTemporaryFile(suffix="mp3"))
        temp_image = File(NamedTemporaryFile(suffix="png"))
        temp_audio.name = "test_2_audio.mp3"
        temp_image.name = "test_2_image.png"
        recite.thumbnail_pic = temp_image
        recite.recitation_audio = temp_audio
        recite.save()

    def test_recitation_views(self):
        recitation = Recitation.objects.first()
        recitation2 = Recitation.objects.get(id=2)
        image_path1 = "http://testserver/media/" + recitation.thumbnail_pic.name
        image_path2 = "http://testserver/media/" + recitation2.thumbnail_pic.name
        expected_data = [
            {
                "title": "random title",
                "thumbnail_pic": image_path1,
                "rating": 0.0,
                "id": 1,
            },
            {
                "title": "random title2",
                "thumbnail_pic": image_path2,
                "rating": 0.0,
                "id": 2,
            },
        ]
        expected_json_data = json.dumps(expected_data)
        client = Client()
        response = client.get("/recitations/list/")
        self.assertJSONEqual(response.content, expected_json_data)
