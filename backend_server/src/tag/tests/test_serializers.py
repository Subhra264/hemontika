from django.test.testcases import TestCase
from tag.models import Tag
from rest_framework.renderers import JSONRenderer
from tag.serializers import TagSerializer
import pytest, json


class TestSerializers(TestCase):
    @pytest.mark.django_db
    def test_tag_serializer(self):
        Tag.objects.create(name="horror")
        Tag.objects.create(name="mystry")
        Tag.objects.create(name="comedy")

        serialized_tag = TagSerializer(Tag.objects.all(), many=True)
        json_data = JSONRenderer().render(serialized_tag.data)

        expected_data = [
            {"id": 1, "name": "horror"},
            {"id": 2, "name": "mystry"},
            {"id": 3, "name": "comedy"},
        ]
        expected_data = json.dumps(expected_data)
        self.assertJSONEqual(json_data, expected_data)
