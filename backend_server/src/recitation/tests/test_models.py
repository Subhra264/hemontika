from django.test import TestCase
from recitation.models import Recitation
from tag.models import Tag
from api_app.models import HemontikaUser

# create model related tests here


class TestModels(TestCase):
    def test_recitation_models(self):
        john = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        tag = Tag.objects.create(name="nation")
        recitation = Recitation.objects.create(reciter=john, title="national enthem")
        tag.recitation_set.add(recitation)
        self.assertEqual(recitation.tags.count(), 1)
        Recitation.objects.create(reciter=john, title="any other recitation")
        Recitation.objects.create(reciter=john, title="recitaion instance")
        self.assertEqual(john.recitation_set.count(), 3)
        # TODO: test cases related to required and default fields should also be added
        # TODO: have to add test cases for audio(file) and image fields
