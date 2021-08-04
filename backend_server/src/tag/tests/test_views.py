from tag.models import Tag
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
        response = client.get("/tags/")
        assert response.status_code == 200
        self.assertJSONEqual(response.content, expected_data)
