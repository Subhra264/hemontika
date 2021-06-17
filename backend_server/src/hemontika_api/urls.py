from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/literature/", include("literature.urls")),
    path("api/tags/", include("tag.urls")),
    # path("api/art/", include("art.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
