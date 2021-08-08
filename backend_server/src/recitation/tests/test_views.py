from tag.models import Tag
from tempfile import NamedTemporaryFile
from django.core.files.base import File
from django.test.testcases import TestCase, Client
from rest_framework.utils import json
from recitation.models import Recitation
from freezegun import freeze_time
from django.contrib.auth import get_user_model

HemontikaUser = get_user_model()


@freeze_time("2021-01-01 11:12:13.000000")
class TestViews(TestCase):

    DATE = "2021-01-01T11:12:13Z"

    def test_recitation_views(self):
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        recitaion = Recitation(reciter=jack, title="something here..")
        temp_audio = File(NamedTemporaryFile(suffix="mp3"))
        temp_image = File(NamedTemporaryFile(suffix="jpg"))
        temp_audio.name = "test_audio.mp3"
        temp_image.name = "test_image.jpg"
        recitaion.recitation_audio = temp_audio
        recitaion.front_img = temp_image
        recitaion.save()
        tag1 = Tag.objects.create(name="classics")
        tag2 = Tag.objects.create(name="song")
        tag1.recitation_set.add(recitaion)
        tag2.recitation_set.add(recitaion)
        audio_path = "http://testserver/media/" + recitaion.recitation_audio.name
        image_path = "http://testserver/media/" + recitaion.front_img.name
        expected_data = [
            {
                "id": 1,
                "reciter": 1,
                "title": "something here..",
                "recitation_audio": audio_path,
                "front_img": image_path,
                "date": self.DATE,
                "tags": [1, 2],
            }
        ]
        expected_json_data = json.dumps(expected_data)
        client = Client()
        response = client.get("/recitations/")
        self.assertJSONEqual(response.content, expected_json_data)

        response = client.get("/recitations/1/")
        expected_json_data = json.dumps(expected_data[0])
        self.assertJSONEqual(response.content, expected_json_data)
