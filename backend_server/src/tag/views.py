from rest_framework.generics import ListAPIView
from .models import Tag
from .serializers import TagSerializer


# Create your views here.
class TagApiView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
