from django.test import TestCase
from music.models import Music
from api_app.models import HemontikaUser
from tag.models import Tag


class TestModels(TestCase):
    def test_music_models(self):
        john = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        music = Music.objects.create(musician=john, title="a title song")
        tag = Tag.objects.create(name="Indian Classical Music")
        tag.music_set.add(music)
        Music.objects.create(musician=john, title="another title song")
        Music.objects.create(musician=john, title="bad songs of the year")
        self.assertEqual(tag.music_set.count(), 1)
        self.assertEqual(music.tags.get(id=1), tag)
        self.assertEqual(john.music_set.count(), 3)
        # TODO: add test case for video upload
