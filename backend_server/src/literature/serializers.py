from rest_framework import serializers
from .models import Story, Poem, Book, Novel, Chapter


class NotAllowedModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("exclude_fields", None)
        super().__init__(*args, **kwargs)
        if fields:
            not_allowed = set(fields)
            existing = set(self.fields)
            for field in not_allowed:
                if field in existing:
                    self.fields.pop(field)


class StorySerializer(NotAllowedModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


class PoemSerializer(NotAllowedModelSerializer):
    class Meta:
        model = Poem
        fields = "__all__"


class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = "__all__"


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"


class BookSerializer(NotAllowedModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
