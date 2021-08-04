from django.urls import path
from . import views

urlpatterns = [
    path("", views.TagApiView.as_view(), name="tag.tags"),
]
