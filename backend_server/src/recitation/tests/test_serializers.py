from io import BytesIO
from rest_framework.exceptions import NotAcceptable
from rest_framework.renderers import JSONRenderer
from tag.models import Tag
from tempfile import NamedTemporaryFile
from PIL import Image
from django.core.files.base import File
from django.contrib.auth import get_user_model
from django.test.testcases import TestCase
from rest_framework.utils import json
from recitation.models import Recitation
from django.db import transaction
from django.core.files.uploadedfile import SimpleUploadedFile
from recitation.serializers import (
    ListRecitationSerializer,
    RetrieveRecitationSerializer,
    CreateDestroyRecitationSerializer,
    UpdateRecitationSerializer,
)
from freezegun import freeze_time
from pytest import importorskip

importorskip("random_hello")
HemontikaUser = get_user_model()


@freeze_time("2021-01-01 11:12:13.000000")
class TestSerializers(TestCase):

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

    def test_list_recitation_serializers(self):
        json_data = JSONRenderer().render(ListRecitationSerializer(Recitation.objects.all(), many=True).data)
        recitattion1 = Recitation.objects.first()
        recitation2 = Recitation.objects.get(id=2)
        image_path1 = "/media/" + recitattion1.thumbnail_pic.name
        image_path2 = "/media/" + recitation2.thumbnail_pic.name
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
        self.assertJSONEqual(json_data, expected_json_data)
        with transaction.atomic():
            with self.assertRaises(NotAcceptable):
                serializer = ListRecitationSerializer(data=expected_data[1])
                serializer.is_valid(raise_exception=True)
                serializer.save(reciter=HemontikaUser.objects.first(), description="random desc", language="en")
            with self.assertRaises(NotAcceptable):
                serializer = ListRecitationSerializer(recitattion1, expected_data[1])
                serializer.is_valid(raise_exception=True)
                serializer.save()

    def test_retrieve_recitation_serializers(self):
        recitation = Recitation.objects.first()
        json_data = JSONRenderer().render(RetrieveRecitationSerializer(recitation).data)
        audio_path = "/media/" + recitation.recitation_audio.name
        image_path = "/media/" + recitation.thumbnail_pic.name
        expected_data = {
            "id": 1,
            "reciter": 1,
            "title": "random title",
            "recitation_audio": audio_path,
            "thumbnail_pic": image_path,
            "date": self.DATE,
            "rating": 0.0,
            "views": 0,
            "description": "random description",
            "language": "en",
            "tags": [1, 2],
        }
        expected_json_data = json.dumps(expected_data)
        self.assertJSONEqual(json_data, expected_json_data)
        with transaction.atomic():
            with self.assertRaises(NotAcceptable):
                serializer = RetrieveRecitationSerializer(data=expected_data)
                serializer.is_valid(raise_exception=True)
                serializer.save(reciter=HemontikaUser.objects.first(), description="random desc", language="en")
            with self.assertRaises(NotAcceptable):
                serializer = RetrieveRecitationSerializer(recitation, expected_data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

    def test_create_destroy_recitation_serializers(self):
        json_data = CreateDestroyRecitationSerializer(Recitation.objects.first()).data
        self.assertEqual({}, json_data)
        image = BytesIO()
        Image.new("RGB", (100, 100)).save(image, "JPEG")
        image.seek(0)
        create_info = {
            "title": "creating recitation",
            "thumbnail_pic": SimpleUploadedFile("test_image.jpg", image.getvalue()),
            "recitation_audio": SimpleUploadedFile("test_audio.mp3", b"some_content", content_type="audio/mp3"),
            "tags": [
                1,
            ],
            "description": "creating recitation description",
            "language": "en",
        }
        serializer = CreateDestroyRecitationSerializer(data=create_info)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        serializer.save(reciter=HemontikaUser.objects.first())
        recitation = Recitation.objects.last()
        self.assertEqual(recitation.pk, 3)
        self.assertEqual(recitation.title, "creating recitation")
        self.assertEqual(recitation.tags.first().pk, 1)
        self.assertEqual(recitation.views, 0)
        self.assertEqual(recitation.rating, 0.0)
        self.assertEqual(recitation.description, "creating recitation description")
        with transaction.atomic():
            with self.assertRaises(NotAcceptable):
                create_info["thumbnail_pic"] = SimpleUploadedFile("test_image2.jpg", image.getvalue())
                serializer = CreateDestroyRecitationSerializer(Recitation.objects.first(), data=create_info)
                serializer.is_valid(raise_exception=True)
                serializer.save()

    def test_update_recitation_serializer(self):
        recitation = Recitation.objects.first()
        image = BytesIO()
        Image.new("RGB", (100, 100)).save(image, "JPEG")
        image.seek(0)
        update_info = {
            "title": "creating recitation",
            "thumbnail_pic": SimpleUploadedFile("test_image.jpg", image.getvalue()),
            "tags": [
                1,
            ],
            "description": "creating recitation description",
        }
        serializer = UpdateRecitationSerializer(recitation, data=update_info)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        serializer.save()
        self.assertEqual(recitation.title, "creating recitation")
        self.assertRegex(recitation.thumbnail_pic.name, r"images/recitations/_1_test_image()|(_([0-9a-zA-Z]){7}).jpg")
        self.assertEqual(recitation.tags.count(), 1),
        self.assertEqual(recitation.tags.first(), Tag.objects.get(id=1))
        self.assertEqual(recitation.description, "creating recitation description")
        self.assertRegex(
            recitation.recitation_audio.name, r"videos/recitations/_1_test_audio()|(_([0-9a-zA-Z]){7}).mp3"
        )
        update_info["views"] = 40
        serializer = UpdateRecitationSerializer(recitation, data=update_info)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(Exception):
            serializer.save()
        self.assertEqual(recitation.views, 0)
        with self.assertRaises(NotAcceptable):
            update_info["thumbnail_pic"] = SimpleUploadedFile("test_image2.jpg", image.getvalue())
            recitation_audio = File(NamedTemporaryFile(suffix="mp3"))
            recitation_audio.name = "test_audio1.mp3"
            serializer = UpdateRecitationSerializer(data=update_info)
            serializer.is_valid(raise_exception=True)
            serializer.save(reciter=HemontikaUser.objects.first(), recitation_audio=recitation_audio, language="en")
