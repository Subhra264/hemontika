import os
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import transaction
from recitation.models import Recitation
from tag.models import Tag
from django.contrib.auth import get_user_model

# create model related tests here

HemontikaUser = get_user_model()


class TestModels(TestCase):
    def test_recitation_models(self):
        audio_path = os.path.join(os.path.dirname(__file__), "assets/test_audio.mp3")
        john = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        tag = Tag.objects.create(name="nation")
        recitation = Recitation(reciter=john, title="national enthem")
        recitation.recitation_audio = SimpleUploadedFile(
            name="test_audio.mp3", content=open(audio_path, "rb").read(), content_type="audio"
        )
        recitation.save()
        tag.recitation_set.add(recitation)
        self.assertEqual(recitation.tags.count(), 1)
        self.assertRegex(
            recitation.recitation_audio.name, r"videos/recitations/_1_test_audio()|(_([0-9a-zA-Z]){7}).mp3"
        )
        Recitation.objects.create(reciter=john, title="any other recitation")
        Recitation.objects.create(reciter=john, title="recitaion instance")
        self.assertEqual(john.recitation_set.count(), 3)
        with transaction.atomic():
            self.assertRaises(Exception, Recitation.objects.create(reciter=john, title="no audio files"))
