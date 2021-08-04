from .models import Art
from rest_framework.viewsets import ModelViewSet
from .serializers import ArtSerializer


class ArtViewSet(ModelViewSet):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    http_method_names = ["get", "post", "patch", "delete", "head"]
