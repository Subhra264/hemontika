from art.models import Art
from tag.models import Tag
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.core.files import File
from freezegun import freeze_time
from tempfile import NamedTemporaryFile
import json

HemontikaUser = get_user_model()


@freeze_time("2021-01-01 11:12:13.000000")
class TestViews(TestCase):

    DATE = "2021-01-01T11:12:13Z"

    def test_art_views(self):
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        client = Client()
        art = Art(artist=jack, title="something here..")
        temp_img = File(NamedTemporaryFile(suffix="jpg"))
        temp_img.name = "test_image.jpg"
        art.image = temp_img
        art.save()
        tag1 = Tag.objects.create(name="ancient painting")
        tag2 = Tag.objects.create(name="water color")
        tag1.art_set.add(art)
        tag2.art_set.add(art)
        image_path = "http://testserver/media/" + art.image.name
        expected_data = [
            {
                "id": 1,
                "artist": 1,
                "title": "something here..",
                "image": image_path,
                "date": self.DATE,
                "tags": [1, 2],
            }
        ]
        expected_json_data = json.dumps(expected_data)
        response = client.get("/arts/")
        self.assertJSONEqual(response.content, expected_json_data)

        response = client.get("/arts/1/")
        expected_json_data = json.dumps(expected_data[0])
        self.assertJSONEqual(response.content, expected_json_data)
