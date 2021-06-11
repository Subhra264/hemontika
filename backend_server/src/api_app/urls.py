from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("novels/", views.NovelsApiView.as_view(), name="api_app.novels"),
    path("poems/", views.PoemsApiView.as_view(), name="api_app.poems"),
    path("stories/", views.StoriesApiView.as_view(), name="api_app.novels"),
    path("books/", views.BooksApiView.as_view(), name="api_app.books"),
    path("novels/<int:pk>/", views.GetNovelApiView.as_view(), name="api_app.get_novel"),
    path("books/<int:pk>/", views.GetBookApiView.as_view(), name="api_app.get_book"),
    path("poems/<int:pk>/", views.GetPoemApiView.as_view(), name="api_app.get_poem"),
    path("stories/<int:pk>/", views.GetStoryApiView.as_view(), name="api_app.get_story"),
    path("user/<int:pk>/poems/", views.all_poems, name="api_app.user.all_poems"),
    path("user/<int:pk>/stories/", views.all_stories, name="api_app.user.all_stories"),
    path("user/<int:pk>/novels/", views.all_novels, name="api_app.user.all_novels"),
    path("user/<int:pk>/book/", views.all_books, name="api_app.user.all_books"),
]
