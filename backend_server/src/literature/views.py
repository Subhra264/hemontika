from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Story, Poem, Book, Novel
from .serializers import BookSerializer, NovelSerializer, PoemSerializer, StorySerializer

# Create your views here.


def index(request):
    book = Book.objects.all()
    book_serializer = BookSerializer(book, many=True)
    return HttpResponse(JSONRenderer().render(book_serializer.data))


# def novels(requests):

#     return JsonResponse({'message': 'hello'})
class NovelsApiView(APIView):
    def get(self, request, format=None):
        novels = Novel.objects.all()
        serialized_novels = NovelSerializer(novels, many=True)
        response = serialized_novels.data
        return Response(response)


class PoemsApiView(APIView):
    def get(self, request, format=None):
        poems = Poem.objects.all()
        serialized_poems = PoemSerializer(poems, many=True, exclude_fields=["content"]).data
        return Response(serialized_poems)


class StoriesApiView(APIView):
    def get(self, request, format=None):
        stories = Story.objects.all()
        serialized_stories = StorySerializer(stories, many=True, exclude_fields=["content"]).data
        return Response(serialized_stories)


class BooksApiView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serialized_books = BookSerializer(books, many=True, exclude_fields=["novels", "stories", "poems"]).data
        return Response(serialized_books)


class GetNovelApiView(APIView):
    pass


class GetPoemApiView(APIView):
    pass


class GetStoryApiView(APIView):
    pass


class GetBookApiView(APIView):
    pass


def all_poems(requests):
    return JsonResponse({"message": "hello"})


def all_stories(requests):
    return JsonResponse({"message": "hello"})


def all_novels(requests):
    return JsonResponse({"message": "hello"})


def all_books(requests):
    return JsonResponse({"message": "hello"})