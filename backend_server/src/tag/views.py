from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tag
from .serializers import TagSerializer
from api_app.models import Novel, Poem, Story, Book


# Create your views here.
class TagsApiView(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serialized_tags = TagSerializer(tags, many=True).data
        return Response(serialized_tags)


class TagApiView(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            try:
                tag = Tag.objects.get(id=pk)
            except Exception as e:
                raise e
            else:
                serialized_tag = TagSerializer(tag).data
                print(serialized_tag)
                novels = Novel.objects.filter(tags=tag).values_list("id", flat=True)
                poems = Poem.objects.filter(tags=tag).values_list("id", flat=True)
                stories = Story.objects.filter(tags=tag).values_list("id", flat=True)
                books = Book.objects.filter(tags=tag).values_list("id", flat=True)
                serialized_tag["novels"] = novels
                serialized_tag["poems"] = poems
                serialized_tag["stories"] = stories
                serialized_tag["books"] = books
                return Response(serialized_tag)
