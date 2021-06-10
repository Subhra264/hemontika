from api_app.models import HemontikaUser, Story, Poem, Book, Novel, Chapter
from tag.models import Tag
from api_app.serializers import BookSerializer, NovelSerializer, PoemSerializer, StorySerializer, ChapterSerializer
from django.test import TestCase
import pytest, json
from rest_framework.renderers import JSONRenderer
from freezegun import freeze_time


@freeze_time("2021-01-01 11:12:13.000000")
class TestSerializers(TestCase):

    DATE = "2021-01-01T11:12:13Z"

    @pytest.mark.django_db
    def test_story_serializer(self):
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        john = HemontikaUser.objects.create(
            username="johni56", first_name="john", last_name="doe", email="johndoe12@gmail.com", password="kaka@134"
        )
        tag = Tag.objects.create(name="horror")
        tag2 = Tag.objects.create(name="bengali")
        tag3 = Tag.objects.create(name="short stories")

        story = Story.objects.create(author=jack, title="a story about serializer", content="hello all")
        story2 = Story.objects.create(author=jack, title="title", content="sharlock homes")
        Story.objects.create(author=john, title="A man with a twisted lip", content="bla bla bla")
        tag.story_set.set([story, story2])
        tag2.story_set.add(story)
        tag3.story_set.add(story)
        stories = Story.objects.all()
        # FIXME: add ImageField also. Convert this code into efficient and professional code
        serializer1 = StorySerializer(story)
        json_data = JSONRenderer().render(serializer1.data)
        data = {
            "id": 1,
            "title": "a story about serializer",
            "front_img": None,
            "date": self.DATE,
            "content": "hello all",
            "author": 1,
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
                "front_img": None,
                "date": self.DATE,
                "content": "hello all",
                "author": 1,
                "tags": [1, 2, 3],
            },
            {
                "id": 2,
                "title": "title",
                "front_img": None,
                "date": self.DATE,
                "content": "sharlock homes",
                "author": 1,
                "tags": [1],
            },
            {
                "id": 3,
                "title": "A man with a twisted lip",
                "front_img": None,
                "date": self.DATE,
                "content": "bla bla bla",
                "author": 2,
                "tags": [],
            },
        ]
        data = json.dumps(data)
        self.assertJSONEqual(json_data, data)

    @pytest.mark.django_db
    def test_poem_serializer(self):
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        john = HemontikaUser.objects.create(
            username="johni56", first_name="john", last_name="doe", email="johndoe12@gmail.com", password="kaka@134"
        )
        tag = Tag.objects.create(name="poem")
        poem = Poem.objects.create(author=jack, title="blossoms", content=" beautiful blossoms")
        tag.poem_set.add(poem)
        Poem.objects.create(author=john, title="two blossoms", content="hello blossoms")
        Poem.objects.create(author=john, title="three blossoms", content="happy blossoms")
        serializer1 = PoemSerializer(poem)
        data = {
            "id": 1,
            "title": "blossoms",
            "front_img": None,
            "date": self.DATE,
            "content": " beautiful blossoms",
            "author": 1,
            "tags": [1],
        }
        data = json.dumps(data)
        json_data = JSONRenderer().render(serializer1.data)
        self.assertJSONEqual(json_data, data)
        serializer2 = PoemSerializer(Poem.objects.all(), many=True)
        data = [
            {
                "id": 1,
                "title": "blossoms",
                "front_img": None,
                "date": self.DATE,
                "content": " beautiful blossoms",
                "author": 1,
                "tags": [1],
            },
            {
                "id": 2,
                "title": "two blossoms",
                "front_img": None,
                "date": self.DATE,
                "content": "hello blossoms",
                "author": 2,
                "tags": [],
            },
            {
                "id": 3,
                "title": "three blossoms",
                "front_img": None,
                "date": self.DATE,
                "content": "happy blossoms",
                "author": 2,
                "tags": [],
            },
        ]
        data = json.dumps(data)
        json_data = JSONRenderer().render(serializer2.data)
        self.assertJSONEqual(json_data, data)

    # def date_converter(self,obj):
    #     if isinstance(obj, datetime):
    #         return obj.__str__()

    @pytest.mark.django_db
    def test_novel_serializer(self):
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        john = HemontikaUser.objects.create(
            username="johni56", first_name="john", last_name="doe", email="johndoe12@gmail.com", password="kaka@134"
        )
        tag = Tag.objects.create(name="novel")
        novel = Novel.objects.create(author=jack, title="A novel NOT about testing")
        tag.novel_set.add(novel)
        novel.create_chapter(content="somthing here...")
        novel.create_chapter(content="somthing here too ...")

        novel2 = Novel.objects.create(author=john, title="Another novel")
        novel2.create_chapter(content="anything important")
        novel2.create_chapter(content="testing novel serializer")
        novel2.create_chapter(content="hello novel")

        serializer = NovelSerializer(novel)
        data = {
            "id": 1,
            "title": "A novel NOT about testing",
            "front_img": None,
            "date": self.DATE,
            "number_of_chapters": 2,
            "author": 1,
            "tags": [
                1,
            ],
        }
        data = json.dumps(data)
        json_data = JSONRenderer().render(serializer.data)
        self.assertJSONEqual(json_data, data)

        serializer2 = NovelSerializer(Novel.objects.all(), many=True)
        data = [
            {
                "id": 1,
                "title": "A novel NOT about testing",
                "front_img": None,
                "date": self.DATE,
                "number_of_chapters": 2,
                "author": 1,
                "tags": [
                    1,
                ],
            },
            {
                "id": 2,
                "title": "Another novel",
                "front_img": None,
                "date": self.DATE,
                "number_of_chapters": 3,
                "author": 2,
                "tags": [],
            },
        ]
        data = json.dumps(data)
        json_data = JSONRenderer().render(serializer2.data)
        self.assertJSONEqual(json_data, data)

    @pytest.mark.django_db
    def test_chapter_serializer(self):
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        novel = Novel.objects.create(author=jack, title="A novel about testing")
        chapter1 = novel.create_chapter(content="hello chapter")
        novel.create_chapter(content="chapter 2")

        serializer1 = ChapterSerializer(chapter1)
        json_data = JSONRenderer().render(serializer1.data)
        data = json.dumps(
            {
                "id": 1,
                "title": "A novel about testing Part- 1",
                "front_img": None,
                "date": self.DATE,
                "content": "hello chapter",
                "author": 1,
                "previous_chapter": None,
                "novel": 1,
                "tags": [],
            }
        )
        self.assertJSONEqual(json_data, data)

        serializer2 = ChapterSerializer(Chapter.objects.all(), many=True)
        json_data = JSONRenderer().render(serializer2.data)
        data = [
            {
                "id": 1,
                "title": "A novel about testing Part- 1",
                "front_img": None,
                "date": self.DATE,
                "content": "hello chapter",
                "author": 1,
                "previous_chapter": None,
                "novel": 1,
                "tags": [],
            },
            {
                "id": 2,
                "title": "A novel about testing Part- 2",
                "front_img": None,
                "date": self.DATE,
                "content": "chapter 2",
                "author": 1,
                "previous_chapter": 1,
                "novel": 1,
                "tags": [],
            },
        ]
        data = json.dumps(data)
        self.assertJSONEqual(json_data, data)

    @pytest.mark.django_db
    def test_book_serializer(self):
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )

        novel = Novel.objects.create(author=jack, title="A novel about testing")

        poem1 = Poem.objects.create(author=jack, title="blossoms", content="hello blossoms")
        poem2 = Poem.objects.create(author=jack, title="two blossoms", content="happy blossoms")
        story = Story.objects.create(author=jack, title="a story about serializer", content="hello all")

        book = Book.objects.create(author=jack, title=" a book about testing")
        book.add_contents([novel, poem1, poem2, story])

        serializer = BookSerializer(book)
        json_data = JSONRenderer().render(serializer.data)

        data = {
            "id": 1,
            "title": " a book about testing",
            "front_img": None,
            "date": self.DATE,
            "number_of_contents": 4,
            "author": 1,
            "tags": [],
            "novels": [1],
            "stories": [1],
            "poems": [1, 2],
        }
        data = json.dumps(data)
        self.assertJSONEqual(json_data, data)
