from django.urls import path
from . import views

urlpatterns = [
    path("", views.TagsApiView.as_view(), name="tag.tags"),
    path("<int:pk>/", views.TagApiView.as_view(), name="tag.tag"),
]
