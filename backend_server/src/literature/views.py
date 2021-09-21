from django.core.exceptions import ImproperlyConfigured
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Story, Poem, DragDropSelectBook, Novel
from .serializers import DragDropSelectBookSerializer, NovelSerializer, PoemSerializer, StorySerializer

# Create your views here.

class LiteratureAPIView(APIView):
    include_fields = None
    exclude_fields = None
    
    def get_serializer_context(self):
        extra_context = super().get_serializer_context()
        if not self.include_fields and not self.exclude_fields:
            msg = "'%s' must define include_fields or exclude_fields"
            raise ImproperlyConfigured(msg % self.__class__.__name__)
        elif self.include_fields and self.exclude_fields:
            msg = "'%s' can not define both include_fields and exclude_fields"
            raise ImproperlyConfigured(msg % self.__class__.__name__)
        elif self.exclude_fields:
            extra_context["exclude_fields"] = self.exclude_fields
        else:
            extra_context["include_fields"] = self.include_fields
        return extra_context

    def get_queryset(self):
        lang = self.kwargs.get("lang")
        return super().get_queryset().filter(language=lang)


class ShortLiteratureView(ListAPIView, LiteratureAPIView):
    include_fields = ["thumbnail_pic", "title", "rating", "catagory", "read_time"]

    
class StoryListView(ShortLiteratureView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class PoemListView(ShortLiteratureView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer


class NovelListView(LiteratureAPIView):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
    include_fields = ["thumbnail_pic", "title", "rating", "catagory", "number_of_chapters"]


class BookViewSet(ModelViewSet):
    queryset = DragDropSelectBook.objects.all()
    serializer_class = DragDropSelectBookSerializer
    http_method_names = ["get", "post", "patch", "delete", "head"]

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            kwargs["exclude_fields"] = ["novels", "poems", "stories"]
        return super().get_serializer(*args, **kwargs)
