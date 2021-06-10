from django.test import TestCase
from art.models import Art
from api_app.models import HemontikaUser
from tag.models import Tag


class TestModels(TestCase):
    def test_art_models(self):
        john = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        tag = Tag.objects.create(name="oil painting")
        oil_paint = Art.objects.create(artist=john, title="How to paint like Bob Ross?")
        tag.art_set.add(oil_paint)
        self.assertEqual(oil_paint.title, "How to paint like Bob Ross?")
        self.assertEqual(oil_paint.tags.get(id=1), tag)
        Art.objects.create(artist=john, title="I wanna paint!")
        self.assertEqual(Art.objects.count(), 2)
        self.assertEqual(john.art_set.count(), 2)
