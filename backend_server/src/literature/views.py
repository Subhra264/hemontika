from rest_framework.viewsets import ModelViewSet
from .models import Story, Poem, Book, Novel
from .serializers import BookSerializer, NovelSerializer, PoemSerializer, StorySerializer

# Create your views here.


def index(request):
    pass


class NovelViewSet(ModelViewSet):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
    http_method_names = ["get", "post", "patch", "delete", "head"]


class PoemViewSet(ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    http_method_names = ["get", "post", "patch", "delete", "head"]

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            kwargs["exclude_fields"] = ["content"]
        return super().get_serializer(*args, **kwargs)


class StoryViewSet(ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    http_method_names = ["get", "post", "patch", "delete", "head"]

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            kwargs["exclude_fields"] = ["content"]
        return super().get_serializer(*args, **kwargs)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ["get", "post", "patch", "delete", "head"]

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            kwargs["exclude_fields"] = ["novels", "poems", "stories"]
        return super().get_serializer(*args, **kwargs)
