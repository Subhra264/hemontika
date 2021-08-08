from tempfile import NamedTemporaryFile
from django.test import TestCase
from django.core.files import File
from music.models import Music
from tag.models import Tag
from django.contrib.auth import get_user_model

HemontikaUser = get_user_model()


class TestModels(TestCase):
    def test_music_models(self):
        john = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        music = Music(musician=john, title="a title song")
        temp_video = File(NamedTemporaryFile(suffix="mp4"))
        temp_video.name = "test_music.mp4"
        music.video = temp_video
        music.save()
        tag = Tag.objects.create(name="Indian Classical Music")
        tag.music_set.add(music)
        self.assertRegex(music.video.name, r"videos/musics/_1_test_music()|(_([0-9a-zA-z]){7}).mp4")
        Music.objects.create(musician=john, title="another title song")
        Music.objects.create(musician=john, title="bad songs of the year")
        self.assertEqual(tag.music_set.count(), 1)
        self.assertEqual(music.tags.get(id=1), tag)
        self.assertEqual(john.music_set.count(), 3)
        # TODO: add test case for video upload
