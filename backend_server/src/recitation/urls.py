from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.ListRecitationView.as_view(), name="recitation.recitations"),
    path("create", views.CreateRecitationView.as_view(), name="recitation.create"),
    path("recitation/<int:pk>/", views.RetrieveUpdateDeleteRecitationView.as_view(), name="recitation.recitations_update_delete")
]
