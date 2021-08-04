from .models import Recitation
from .serializers import RecitationSerializer
from rest_framework.viewsets import ModelViewSet


class RecitationViewSet(ModelViewSet):
    queryset = Recitation.objects.all()
    serializer_class = RecitationSerializer
    http_method_names = ["get", "post", "patch", "delete", "head"]
