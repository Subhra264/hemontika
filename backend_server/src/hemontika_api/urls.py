from django.contrib import admin
from literature.urls import router as literature_router
from art.urls import router as art_router
from music.urls import router as music_router
from recitation.urls import router as recitation_router
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.registry.extend(literature_router.registry)
router.registry.extend(art_router.registry)
router.registry.extend(music_router.registry)
router.registry.extend(recitation_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("literature/", include("literature.urls")),
    path("", include(router.urls)),
    path("tags/", include("tag.urls")),
]
