from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable


COUNTRY_CHOICES = [
    ("IN", "INDIA"),
    ("USA", "UNITED sTATES"),
]

REGION_CHOICES = [
    ("WB", "WEST BENGAL"),
    ("UP", "UTTAR PRADESH"),
    ("MP", "MADHYA PRADESH"),
    ("TN", "TAMILNADU"),
]

DISTRICT_CHOICES = [
    ("HOW", "HOWRAH"),
    ("HOO", "HOOGLY"),
    ("KOL", "KOLKATA"),
]


class ReadOnlyModelSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        for field in fields:
            fields[field].read_only = True
        return fields

    def create(self, validated_data):
        raise NotAcceptable("This serializer can't be used for creation")

    def update(self, instance, validated_data):
        raise NotAcceptable("This serializer can't be used for updatation")


class CreateDestroyModelSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        for field in fields:
            fields[field].write_only = True
        return fields

    def update(self, instance, validated_data):
        raise NotAcceptable("Updatation is not allowed with this serializer")


class UpdateOnlyModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs["partial"] = True
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        raise NotAcceptable("This serializer can't be used for creation")
