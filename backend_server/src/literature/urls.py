from django.urls import path
from .views import StoryListView, PoemListView, NovelListView, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path(r"^literature/catagories/novels", NovelListView.as_view(), name="literature.catagories.novels"),
    path(r"^literature/catagories/poems", PoemListView.as_view(), name="literature.catagories.poems"),
    path(r"^literature/catagories/stories", StoryListView.as_view(), name="literature.catagories.stories"),
]

router.register(r"^literature/catagories/books", BookViewSet, basename="literature.catagories.books")
