from tag.models import Tag
from api_app.models import Story, HemontikaUser
from django.test import TestCase, Client
import json
from freezegun import freeze_time


@freeze_time("2021-01-01 11:12:13.000000")
class TestViews(TestCase):
    """tests for views"""

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="horror")
        Tag.objects.create(name="mystry")
        Tag.objects.create(name="fiction")
        Tag.objects.create(name="crime")

    def test_tags_view(self):
        client = Client()

        expected_data = [
            {
                "id": 1,
                "name": "horror",
            },
            {"id": 2, "name": "mystry"},
            {"id": 3, "name": "fiction"},
            {"id": 4, "name": "crime"},
        ]

        expected_data = json.dumps(expected_data)
        response = client.get("/api/tags/")
        assert response.status_code == 200
        self.assertJSONEqual(response.content, expected_data)

    def test_tag_view(self):
        client = Client()
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        story = Story.objects.create(author=jack, title="a story about serializer", content="hello all")

        tag = Tag.objects.get(id=1)
        tag.story_set.add(story)
        expected_data = {"id": 1, "name": "horror", "poems": [], "novels": [], "stories": [1], "books": []}
        expected_data = json.dumps(expected_data)
        response = client.get("/api/tags/1/")
        self.assertJSONEqual(response.content, expected_data)
