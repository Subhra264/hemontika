from django.test import TestCase
from django.contrib.auth import get_user_model
from user.models import Profile

HemontikaUser = get_user_model()


class TestModels(TestCase):
    def test_profile_models(self):
        john = HemontikaUser.objects.create(username="john@123", password="12345", email="john@doe.com")
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.get(id=1).user, john)
        john.delete()
        self.assertEqual(Profile.objects.count(), 0)
