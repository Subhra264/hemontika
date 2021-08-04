from rest_framework.utils import json
from music.models import Music
from django.test import TestCase, Client
from literature.models import HemontikaUser
from django.core.files import File
from tempfile import NamedTemporaryFile
from tag.models import Tag
from freezegun import freeze_time


@freeze_time("2021-01-01 11:12:13.000000")
class TestViews(TestCase):

    DATE = "2021-01-01T11:12:13Z"

    def test_music_views(self):
        client = Client()
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        music = Music(musician=jack, title="something here..")
        temp_vid = File(NamedTemporaryFile(suffix="mp4"))
        temp_vid.name = "test_video.mp4"
        music.video = temp_vid
        music.save()
        tag1 = Tag.objects.create(name="classics")
        tag2 = Tag.objects.create(name="song")
        tag1.music_set.add(music)
        tag2.music_set.add(music)
        video_path = "http://testserver/media/" + music.video.name
        expected_data = [
            {
                "id": 1,
                "musician": 1,
                "title": "something here..",
                "video": video_path,
                "date": self.DATE,
                "tags": [1, 2],
            }
        ]
        expected_json_data = json.dumps(expected_data)
        response = client.get("/musics/")
        self.assertJSONEqual(response.content, expected_json_data)

        expected_json_data = json.dumps(expected_data[0])
        response = client.get("/musics/1/")
        self.assertJSONEqual(response.content, expected_json_data)
