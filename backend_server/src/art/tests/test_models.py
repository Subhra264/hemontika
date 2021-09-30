import os
from django.db import transaction
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from art.models import Art
from tag.models import Tag
from django.contrib.auth import get_user_model

HemontikaUser = get_user_model()


class TestModels(TestCase):
    def test_art_models(self):
        image_path = os.path.join(os.path.dirname(__file__), "img/test_art.png")
        john = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        tag = Tag.objects.create(name="oil painting")
        oil_paint = Art(artist=john, title="How to paint like Bob Ross?")
        oil_paint.description = "this is the description"
        oil_paint.image = SimpleUploadedFile(
            name="test_art.png", content=open(image_path, "rb").read(), content_type="image"
        )
        oil_paint.save()
        tag.art_set.add(oil_paint)
        self.assertEqual(oil_paint.title, "How to paint like Bob Ross?")
        self.assertEqual(oil_paint.tags.get(id=1), tag)
        self.assertEqual(oil_paint.rating, 0.0)
        self.assertEqual(oil_paint.views, 0)
        self.assertFalse(bool(oil_paint.region))
        self.assertFalse(bool(oil_paint.district))
        self.assertFalse(bool(oil_paint.country))
        self.assertRegex(oil_paint.image.name, r"images/arts/_1_test_art()|(_([0-9a-zA-Z]){7}).png")
        with transaction.atomic():
            self.assertRaises(Exception, Art.objects.create(artist=john, title="I wanna paint!"))
