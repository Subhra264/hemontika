from literature.models import Story, Poem, DragDropSelectBook, Novel, Chapter
from tag.models import Tag
from literature.serializers import (
    DragDropSelectBookSerializer,
    NovelSerializer,
    PoemSerializer,
    StorySerializer,
    ChapterSerializer,
)
from django.test import TestCase
import pytest, json
from tempfile import NamedTemporaryFile
from rest_framework.renderers import JSONRenderer
from django.core.files import File
from django.contrib.auth import get_user_model
from freezegun import freeze_time

HemontikaUser = get_user_model()


def return_image_path(instance):
    return "/media/" + instance.thumbnail_pic.name


@freeze_time("2021-01-01 11:12:13.000000")
class TestSerializers(TestCase):

    DATE = "2021-01-01T11:12:13Z"

    def setUp(self):
        self.jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        self.john = HemontikaUser.objects.create(
            username="johni56", first_name="john", last_name="doe", email="johndoe12@gmail.com", password="kaka@134"
        )
        self.temp_image = File(NamedTemporaryFile(suffix="jpg"))
        self.temp_image.name = "test_image.jpg"

    @pytest.mark.django_db
    def test_story_serializer(self):
        tag = Tag.objects.create(name="horror")
        tag2 = Tag.objects.create(name="bengali")
        tag3 = Tag.objects.create(name="short stories")

        story = Story.objects.create(
            author=self.jack,
            title="a story about serializer",
            content="hello all",
            description="This is the description",
            language="en",
            catagory="oth",
        )
        story2 = Story(author=self.jack, title="title", content="sharlock homes")
        story2.thumbnail_pic = self.temp_image
        story2.language = "en"
        story2.catagory = "oth"
        story2.description = "This is the description"
        story2.save()
        Story.objects.create(
            author=self.john,
            title="A man with a twisted lip",
            content="bla bla bla",
            description="This is the description",
            language="en",
            catagory="oth",
        )
        tag.story_set.set([story, story2])
        tag2.story_set.add(story)
        tag3.story_set.add(story)
        stories = Story.objects.all()
        serializer1 = StorySerializer(story)
        json_data = JSONRenderer().render(serializer1.data)
        data = {
            "id": 1,
            "title": "a story about serializer",
            "thumbnail_pic": None,
            "created_at": self.DATE,
            "updated_at": self.DATE,
            "content": "hello all",
            "author": 1,
            "rating": 0.0,
            "description": "This is the description",
            "read_time": 0,
            "language": "en",
            "catagory": "oth",
            "views": 0,
            "tags": [1, 2, 3],
        }
        data = json.dumps(data)
        self.assertJSONEqual(json_data, data)

        serializer2 = StorySerializer(stories, many=True)
        json_data = JSONRenderer().render(serializer2.data)
        data = [
            {
                "id": 1,
                "title": "a story about serializer",
                "thumbnail_pic": None,
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "content": "hello all",
                "author": 1,
                "rating": 0.0,
                "description": "This is the description",
                "read_time": 0,
                "language": "en",
                "catagory": "oth",
                "views": 0,
                "tags": [1, 2, 3],
            },
            {
                "id": 2,
                "title": "title",
                "thumbnail_pic": return_image_path(story2),
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "content": "sharlock homes",
                "author": 1,
                "tags": [1],
                "rating": 0.0,
                "description": "This is the description",
                "read_time": 0,
                "language": "en",
                "catagory": "oth",
                "views": 0,
            },
            {
                "id": 3,
                "title": "A man with a twisted lip",
                "thumbnail_pic": None,
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "content": "bla bla bla",
                "author": 2,
                "tags": [],
                "rating": 0.0,
                "description": "This is the description",
                "read_time": 0,
                "language": "en",
                "catagory": "oth",
                "views": 0,
            },
        ]
        self.maxDiff = None
        data = json.dumps(data)
        self.assertJSONEqual(json_data, data)

    @pytest.mark.django_db
    def test_poem_serializer(self):
        tag = Tag.objects.create(name="poem")
        poem = Poem.objects.create(
            author=self.jack,
            title="blossoms",
            content=" beautiful blossoms",
            description="This is the description",
            language="en",
            catagory="oth",
        )
        tag.poem_set.add(poem)
        poem2 = Poem(
            author=self.john,
            title="two blossoms",
            content="hello blossoms",
            description="This is the description",
            language="en",
            catagory="oth",
        )
        poem2.thumbnail_pic = self.temp_image
        poem2.save()
        serializer1 = PoemSerializer(poem)
        data = {
            "id": 1,
            "title": "blossoms",
            "thumbnail_pic": None,
            "created_at": self.DATE,
            "updated_at": self.DATE,
            "content": " beautiful blossoms",
            "author": 1,
            "tags": [1],
            "rating": 0.0,
            "description": "This is the description",
            "read_time": 0,
            "language": "en",
            "catagory": "oth",
            "views": 0,
        }
        data = json.dumps(data)
        json_data = JSONRenderer().render(serializer1.data)
        self.assertJSONEqual(json_data, data)
        serializer2 = PoemSerializer(Poem.objects.all(), many=True)
        data = [
            {
                "id": 1,
                "title": "blossoms",
                "thumbnail_pic": None,
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "content": " beautiful blossoms",
                "author": 1,
                "tags": [1],
                "rating": 0.0,
                "description": "This is the description",
                "read_time": 0,
                "language": "en",
                "catagory": "oth",
                "views": 0,
            },
            {
                "id": 2,
                "title": "two blossoms",
                "thumbnail_pic": return_image_path(poem2),
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "content": "hello blossoms",
                "author": 2,
                "tags": [],
                "rating": 0.0,
                "description": "This is the description",
                "read_time": 0,
                "language": "en",
                "catagory": "oth",
                "views": 0,
            },
        ]
        data = json.dumps(data)
        json_data = JSONRenderer().render(serializer2.data)
        self.assertJSONEqual(json_data, data)

    @pytest.mark.django_db
    def test_novel_serializer(self):
        tag = Tag.objects.create(name="novel")
        novel = Novel.objects.create(
            author=self.jack,
            title="A novel NOT about testing",
            description="This is the description",
            language="en",
            catagory="oth",
        )
        tag.novel_set.add(novel)
        novel.create_chapter(content="somthing here...")
        novel.create_chapter(content="somthing here too ...")

        novel2 = Novel(author=self.john, title="Another novel")
        novel2.thumbnail_pic = self.temp_image
        novel2.description = "This is the description"
        novel2.catagory = "oth"
        novel2.language = "en"
        novel2.create_chapter(content="anything important")
        novel2.create_chapter(content="testing novel serializer")
        novel2.create_chapter(content="hello novel")

        serializer = NovelSerializer(novel)
        data = {
            "id": 1,
            "title": "A novel NOT about testing",
            "thumbnail_pic": None,
            "created_at": self.DATE,
            "updated_at": self.DATE,
            "number_of_chapters": 2,
            "author": 1,
            "tags": [
                1,
            ],
            "rating": 0.0,
            "description": "This is the description",
            "language": "en",
            "catagory": "oth",
            "views": 0,
        }
        data = json.dumps(data)
        json_data = JSONRenderer().render(serializer.data)
        self.assertJSONEqual(json_data, data)

        serializer2 = NovelSerializer(Novel.objects.all(), many=True)
        data = [
            {
                "id": 1,
                "title": "A novel NOT about testing",
                "thumbnail_pic": None,
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "number_of_chapters": 2,
                "author": 1,
                "tags": [
                    1,
                ],
                "rating": 0.0,
                "description": "This is the description",
                "language": "en",
                "catagory": "oth",
                "views": 0,
            },
            {
                "id": 2,
                "title": "Another novel",
                "thumbnail_pic": return_image_path(novel2),
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "number_of_chapters": 3,
                "author": 2,
                "tags": [],
                "rating": 0.0,
                "description": "This is the description",
                "language": "en",
                "catagory": "oth",
                "views": 0,
            },
        ]
        data = json.dumps(data)
        json_data = JSONRenderer().render(serializer2.data)
        self.assertJSONEqual(json_data, data)

    @pytest.mark.django_db
    def test_chapter_serializer(self):
        novel = Novel.objects.create(author=self.jack, title="A novel about testing")
        chapter1 = novel.create_chapter(content="hello chapter")
        novel.create_chapter(content="chapter 2")
        novel2 = Novel(author=self.jack, title="another novel for image")
        novel2.thumbnail_pic = self.temp_image
        novel2.save()
        chapter2 = novel2.create_chapter(content="chapter 1")

        serializer1 = ChapterSerializer(chapter1)
        json_data = JSONRenderer().render(serializer1.data)
        data = json.dumps(
            {
                "id": 1,
                "title": "A novel about testing Part- 1",
                "thumbnail_pic": None,
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "content": "hello chapter",
                "previous_chapter": None,
                "novel": 1,
            }
        )
        self.assertJSONEqual(json_data, data)

        serializer2 = ChapterSerializer(Chapter.objects.all(), many=True)
        json_data = JSONRenderer().render(serializer2.data)
        data = [
            {
                "id": 1,
                "title": "A novel about testing Part- 1",
                "thumbnail_pic": None,
                "content": "hello chapter",
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "previous_chapter": None,
                "novel": 1,
            },
            {
                "id": 2,
                "title": "A novel about testing Part- 2",
                "thumbnail_pic": None,
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "content": "chapter 2",
                "previous_chapter": 1,
                "novel": 1,
            },
            {
                "id": 3,
                "title": "another novel for image Part- 1",
                "thumbnail_pic": return_image_path(chapter2),
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "content": "chapter 1",
                "previous_chapter": None,
                "novel": 2,
            },
        ]
        data = json.dumps(data)
        self.assertJSONEqual(json_data, data)

    @pytest.mark.django_db
    def test_book_serializer(self):
        novel = Novel.objects.create(author=self.jack, title="A novel about testing")

        poem1 = Poem.objects.create(author=self.jack, title="blossoms", content="hello blossoms")
        poem2 = Poem.objects.create(author=self.jack, title="two blossoms", content="happy blossoms")
        story = Story.objects.create(author=self.jack, title="a story about serializer", content="hello all")

        book = DragDropSelectBook.objects.create(author=self.jack, title=" a book about testing")
        book.description = "This is the description"
        book.language = "en"
        book.catagory = "oth"
        book.save()
        book.add_contents([novel, poem1, poem2, story])
        book2 = DragDropSelectBook(author=self.jack, title="publishing a book")
        book2.description = "This is the description"
        book2.language = "en"
        book2.catagory = "oth"
        book2.thumbnail_pic = self.temp_image
        book2.save()
        book2.add_contents([novel, story])
        serializer = DragDropSelectBookSerializer(book)
        json_data = JSONRenderer().render(serializer.data)

        data = {
            "id": 1,
            "title": " a book about testing",
            "thumbnail_pic": None,
            "created_at": self.DATE,
            "updated_at": self.DATE,
            "number_of_contents": 4,
            "author": 1,
            "tags": [],
            "catagory": "oth",
            "language": "en",
            "rating": 0.0,
            "description": "This is the description",
            "views": 0,
            "novels": [1],
            "stories": [1],
            "poems": [1, 2],
        }
        data = json.dumps(data)
        self.assertJSONEqual(json_data, data)
        serializer = DragDropSelectBookSerializer(DragDropSelectBook.objects.all(), many=True).data
        json_data = JSONRenderer().render(serializer)
        data = [
            {
                "id": 1,
                "title": " a book about testing",
                "thumbnail_pic": None,
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "number_of_contents": 4,
                "author": 1,
                "catagory": "oth",
                "language": "en",
                "rating": 0.0,
                "description": "This is the description",
                "views": 0,
                "tags": [],
                "novels": [1],
                "stories": [1],
                "poems": [1, 2],
            },
            {
                "id": 2,
                "title": "publishing a book",
                "thumbnail_pic": return_image_path(book2),
                "created_at": self.DATE,
                "updated_at": self.DATE,
                "number_of_contents": 2,
                "author": 1,
                "tags": [],
                "catagory": "oth",
                "language": "en",
                "rating": 0.0,
                "description": "This is the description",
                "views": 0,
                "novels": [1],
                "stories": [1],
                "poems": [],
            },
        ]
        data = json.dumps(data)
        self.assertJSONEqual(json_data, data)
