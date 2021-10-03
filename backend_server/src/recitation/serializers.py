from hemontika_api.utils import ReadOnlyModelSerializer, UpdateOnlyModelSerializer, CreateDestroyModelSerializer
from .models import Recitation


class ListRecitationSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = Recitation
        fields = ["title", "thumbnail_pic", "rating", "id"]


class RetrieveRecitationSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = Recitation
        fields = "__all__"


class CreateDestroyRecitationSerializer(CreateDestroyModelSerializer):
    class Meta:
        model = Recitation
        fields = ["title", "thumbnail_pic", "recitation_audio", "tags", "description", "language"]


class UpdateRecitationSerializer(UpdateOnlyModelSerializer):
    class Meta:
        model = Recitation
        fields = ["title", "description", "thumbnail_pic", "tags"]
