from .models import Music
from rest_framework import serializers


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = "__all__"
