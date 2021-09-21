from rest_framework import serializers
from .models import Story, Poem, DragDropSelectBook, Novel, Chapter


class LimitFieldModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop("exclude_fields", None)
        include_fields = kwargs.pop("include_fields", None)
        existing = set(self.fields)
        super().__init__(*args, **kwargs)
        if exclude_fields:
            not_allowed = set(exclude_fields)
            for field in not_allowed:
                if field in existing:
                    self.fields.pop(field)
        elif include_fields:
            allowed = set(include_fields)
            for field in self.fields:
                if field not in allowed:
                    self.fields.pop(field)



class StorySerializer(LimitFieldModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


class PoemSerializer(LimitFieldModelSerializer):
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


class DragDropSelectBookSerializer(LimitFieldModelSerializer):
    class Meta:
        model = DragDropSelectBook
        fields = "__all__"
