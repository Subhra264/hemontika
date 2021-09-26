from django.urls import path
from .views import (
    StoryListView,
    PoemListView,
    NovelListView,
    BookViewSet,
    StoryDetailsView,
    PoemDetailsView,
    NovelDetailsView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("catagories/novels/", NovelListView.as_view(), name="literature.catagories.novels"),
    path("catagories/poems/", PoemListView.as_view(), name="literature.catagories.poems"),
    path("catagories/stories/", StoryListView.as_view(), name="literature.catagories.stories"),
    path(
        "catagories/stories/<int:pk>/details/", StoryDetailsView.as_view(), name="literature.catagories.stories.story"
    ),
    path("catagories/poems/<int:pk>/details/", PoemDetailsView.as_view(), name="literature.catagories.poems.poem"),
    path("catagories/novels/<int:pk>/details/", NovelDetailsView.as_view(), name="literature.catagories.novels.novel"),
    # path("literature/catagories/books/<int:pk>/details/", StoryDetailsView.as_view(), name="literature.catagories.books.book"),
]

router.register(r"^literature/catagories/books", BookViewSet, basename="literature.catagories.books")
