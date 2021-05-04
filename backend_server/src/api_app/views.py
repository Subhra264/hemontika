from django.shortcuts import render
from django.http import HttpResponse
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
    print(poem_serializer.data)
    print(story_serializer.data)
    print(novel_serializer.data)
    print(chapter_serializer.data)
    print(book_serializer.data)
    # text = JSONRenderer().render(poem_serializer.data) + '<br/><br/>' + JSONRenderer().render(story_serializer.data) + '<br/><br/>'+ JSONRenderer().render(novel_serializer.data) + '<br/><br/>'+ JSONRenderer().render(chapter_serializer.data) +'<br/><br/>'+JSONRenderer().render(book_serializer.data)
    return HttpResponse(JSONRenderer().render(novel_serializer.data))