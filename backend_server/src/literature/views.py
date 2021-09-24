from django.core.exceptions import ImproperlyConfigured
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Story, Poem, DragDropSelectBook, Novel
from .serializers import DragDropSelectBookSerializer, NovelSerializer, PoemSerializer, StorySerializer

# Create your views here.

class LiteratureAPIView(GenericAPIView):
    include_fields = None
    exclude_fields = None
    
    def get_serializer_context(self):
        extra_context = super().get_serializer_context()
        if self.include_fields and self.exclude_fields:
            msg = "'%s' can not define both include_fields and exclude_fields"
            raise ImproperlyConfigured(msg % self.__class__.__name__)
        elif self.include_fields == "__all__":
            return extra_context
        elif self.exclude_fields:
            if isinstance(self.exclude_fields, list) or isinstance(self.exclude_fields, tuple):
                extra_context["exclude_fields"] = self.exclude_fields
            else:
                raise ImproperlyConfigured("exclude_fields must be a list or tuple")
        else:
            if isinstance(self.include_fields, list) or isinstance(self.include_fields, tuple):
                extra_context["include_fields"] = self.include_fields
            else:
                raise ImproperlyConfigured("include_fields must be a list or tuple")
        return extra_context

    def get_queryset(self):
        lang = self.request.query_params.get('lang')
        if lang:
            return super().get_queryset().filter(language=lang)
        return super().get_queryset()


class ShortLiteratureListView(ListAPIView, LiteratureAPIView):
    include_fields = ["thumbnail_pic", "title", "rating", "catagory", "read_time"]


class StoryListView(ShortLiteratureListView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class PoemListView(ShortLiteratureListView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer


class NovelListView(ListAPIView, LiteratureAPIView):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
    include_fields = ["thumbnail_pic", "title", "rating", "catagory", "number_of_chapters"]


class DetailsView(RetrieveAPIView):
    
    def get_object(self):
        pk = self.kwargs["pk"]
        obj = self.get_queryset().get(pk=pk)
        return obj


class StoryDetailsView(DetailsView, LiteratureAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    exclude_fields = ["content"]


class PoemDetailsView(DetailsView, LiteratureAPIView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    exclude_fields = ["content"]


class NovelDetailsView(DetailsView):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer


class BookViewSet(ModelViewSet):
    queryset = DragDropSelectBook.objects.all()
    serializer_class = DragDropSelectBookSerializer
    http_method_names = ["get", "post", "patch", "delete", "head"]

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            kwargs["exclude_fields"] = ["novels", "poems", "stories"]
        return super().get_serializer(*args, **kwargs)
