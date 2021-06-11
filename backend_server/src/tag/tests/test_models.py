from tag.models import Tag
from django.test import TestCase
import pytest


class TestModels(TestCase):
    @pytest.mark.django_db
    def test_tag_model(self):
        Tag.objects.create(name="mystry")
        Tag.objects.create(name="horror")
        Tag.objects.create(name="suspense")
        Tag.objects.create(name="sci-fi")
        Tag.objects.create(name="adventure")

        self.assertEqual(Tag.objects.count(), 5)
        self.assertEqual(Tag.objects.get(id=1).name, "mystry")
