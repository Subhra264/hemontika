from django.urls import path
from .views import NovelViewSet, PoemViewSet, StoryViewSet, BookViewSet, index
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("", index, name="index"),
]

router.register(r"^literature/novels", NovelViewSet, basename="literature.novels")
router.register(r"^literature/poems", PoemViewSet, basename="literature.poemss")
router.register(r"^literature/stories", StoryViewSet, basename="literature.stories")
router.register(r"^literature/books", BookViewSet, basename="literature.books")
