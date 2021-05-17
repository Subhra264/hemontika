from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from .models import *
from .serializers import *

# Create your views here.

def index(request):
    stories = Story.objects.all()
    poems = Poem.objects.all()
    novels = Novel.objects.all()
    chapters = Chapter.objects.all()
    book = Book.objects.all()
    story_serializer = StorySerializer(stories,many=True)
    poem_serializer = PoemSerializer(poems, many=True)
    novel_serializer = NovelSerializer(novels, many=True)
    chapter_serializer = ChapterSerializer(chapters,many=True)
    book_serializer = BookSerializer(book, many=True)
    return HttpResponse(JSONRenderer().render(book_serializer.data))

def novels(requests):
    
    return JsonResponse({'message': 'hello'})


def poems(requests):
    return JsonResponse({'message': 'hello'})


def stories(requests):
    return JsonResponse({'message': 'hello'})


def books(requests):
    return JsonResponse({'message': 'hello'})

def get_novel(requests):
    return JsonResponse({'message': 'hello'})


def get_poem(requests):
    return JsonResponse({'message': 'hello'})

def get_story(requests):
    return JsonResponse({'message': 'hello'})

def get_book(requests):
    return JsonResponse({'message': 'hello'})

def all_poems(requests):
    return JsonResponse({'message': 'hello'})

def all_stories(requests):
    return JsonResponse({'message': 'hello'})

def all_novels(requests):
    return JsonResponse({'message': 'hello'})

def all_books(requests):
    return JsonResponse({'message': 'hello'})

def tags(requests):
    return JsonResponse({'message': 'hello'})

def tag(requests,pk=None):
    return JsonResponse({'message': 'hello'})