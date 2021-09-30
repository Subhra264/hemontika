from rest_framework.utils import json
from music.serializers import MusicSerializer
from rest_framework.renderers import JSONRenderer
from music.models import Music
from django.test import TestCase
from django.core.files import File
from django.contrib.auth import get_user_model
from tempfile import NamedTemporaryFile
from tag.models import Tag
from freezegun import freeze_time
from pytest import importorskip

importorskip("random_hello")
HemontikaUser = get_user_model()


@freeze_time("2021-01-01 11:12:13.000000")
class TestSerializers(TestCase):

    DATE = "2021-01-01T11:12:13Z"

    def test_music_models(self):
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
        json_data = JSONRenderer().render(MusicSerializer(music).data)
        video_path = "/media/" + music.video.name
        expected_data = {
            "id": 1,
            "musician": 1,
            "title": "something here..",
            "video": video_path,
            "date": self.DATE,
            "tags": [1, 2],
        }
        expected_json_data = json.dumps(expected_data)
        self.assertJSONEqual(json_data, expected_json_data)
