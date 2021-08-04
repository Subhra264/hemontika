from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r"^musics", views.MusicViewSet, basename="music.musics")
