from .models import Recitation
from rest_framework import serializers


class RecitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recitation
        fields = "__all__"
