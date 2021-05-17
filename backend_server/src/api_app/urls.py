from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index, name='index'),

    path('novels/',views.novels, name='api_app.novels'),
    path('poems/', views.poems, name='api_app.poems'),
    path('stories/',views.stories, name='api_app.novels'),
    path('books/', views.books, name='api_app.books'),

    path('novels/<int:pk>/', views.get_novel, name='api_app.get_novel'),
    path('books/<int:pk>/', views.get_book, name= 'api_app.get_book'),
    path('poems/<int:pk>/', views.get_poem, name= 'api_app.get_poem'),
    path('stories/<int:pk>/', views.get_story, name='api_app.get_story'),

    path('user/<int:pk>/poems/',views.all_poems, name='api_app.user.all_poems'),
    path('user/<int:pk>/stories/',views.all_stories, name='api_app.user.all_stories'),
    path('user/<int:pk>/novels/', views.all_novels, name= 'api_app.user.all_novels'),
    path('user/<int:pk>/book/', views.all_books, name='api_app.user.all_books'),

    path('tags/<int:pk>/', views.tag, name= 'api_app.tag'),
    path('tags/',views.tags, name='api_app.tags'),
]
