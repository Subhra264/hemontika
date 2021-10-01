from _pytest.outcomes import importorskip
from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json
from art.serializers import ArtSerializer
from tag.models import Tag
from art.models import Art
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files import File
from freezegun import freeze_time
from tempfile import NamedTemporaryFile

HemontikaUser = get_user_model()
importorskip("random_hello")


@freeze_time("2021-01-01 11:12:13.000000")
class TestSerializers(TestCase):

    DATE = "2021-01-01T11:12:13Z"

    def test_art_serializer(self):
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        art = Art(artist=jack, title="something here..")
        temp_img = File(NamedTemporaryFile(suffix="jpg"))
        temp_img.name = "test_image.jpg"
        art.image = temp_img
        art.save()
        tag1 = Tag.objects.create(name="ancient painting")
        tag2 = Tag.objects.create(name="water color")
        tag1.art_set.add(art)
        tag2.art_set.add(art)
        serialized_data = ArtSerializer(art).data
        json_data = JSONRenderer().render(serialized_data)
        image_path = "/media/" + art.image.name
        expected_data = {
            "id": 1,
            "artist": 1,
            "title": "something here..",
            "image": image_path,
            "date": self.DATE,
            "tags": [1, 2],
        }
        expected_json_data = json.dumps(expected_data)
        self.assertJSONEqual(json_data, expected_json_data)

        art2 = Art(artist=jack, title="my first pastel color")
        art2.image = temp_img
        art2.save()
        serialized_data = ArtSerializer(Art.objects.all(), many=True).data
        json_data = JSONRenderer().render(serialized_data)
        image2_path = "/media/" + art2.image.name
        expected_data = [
            {"id": 1, "artist": 1, "title": "something here..", "image": image_path, "date": self.DATE, "tags": [1, 2]},
            {
                "id": 2,
                "artist": 1,
                "title": "my first pastel color",
                "image": image2_path,
                "date": self.DATE,
                "tags": [],
            },
        ]
        expected_json_data = json.dumps(expected_data)
        self.assertJSONEqual(json_data, expected_json_data)
