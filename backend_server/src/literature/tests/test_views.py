from django.contrib.auth import get_user_model
from literature.models import Story, Poem, DragDropSelectBook, Novel
from django.test import TestCase, Client
import pytest
import json
from freezegun import freeze_time

HemontikaUser = get_user_model()


@freeze_time("2021-01-01 11:12:13.000000")
class TestViews(TestCase):
    """tests for views"""

    DATE = "2021-01-01T11:12:13Z"

    @classmethod
    def setUpTestData(cls):
        HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        HemontikaUser.objects.create(
            username="johni56", first_name="john", last_name="doe", email="johndoe12@gmail.com", password="kaka@134"
        )

    @pytest.mark.django_db
    def test_novel_list_view(self):
        client = Client()

        jack = HemontikaUser.objects.get(pk=1)
        john = HemontikaUser.objects.get(pk=2)
        novel = Novel.objects.create(author=jack, title="A novel NOT about testing", catagory="oth")
        novel.create_chapter(content="somthing here...")
        novel.create_chapter(content="somthing here too ...")

        novel2 = Novel.objects.create(author=john, title="Another novel", catagory="oth")
        novel2.create_chapter(content="anything important")
        novel2.create_chapter(content="testing novel view")
        novel2.create_chapter(content="hello novel")

        expected_data = [
            {
                "id": 1,
                "title": "A novel NOT about testing",
                # "thumbnail_pic": "http://127.0.0.1:8000/front_img.png",
                "thumbnail_pic": None,
                "rating": 0.0,
                "catagory": "oth",
                "number_of_chapters": 2,
            },
            {
                "id": 2,
                "title": "Another novel",
                "thumbnail_pic": None,
                "rating": 0.0,
                "catagory": "oth",
                "number_of_chapters": 3,
            },
        ]
        expected_data = json.dumps(expected_data)
        response = client.get("/literature/catagories/novels/", HTTP_ACCEPT="application/json")
        self.assertJSONEqual(response.content, expected_data)

    @pytest.mark.django_db
    def test_poem_list_view(self):
        client = Client()
        jack = HemontikaUser.objects.get(pk=1)
        john = HemontikaUser.objects.get(pk=2)
        Poem.objects.create(author=jack, title="blossoms", content=" beautiful blossoms", catagory="oth")
        Poem.objects.create(author=john, title="two blossoms", content="hello blossoms", catagory="oth")
        Poem.objects.create(author=john, title="three blossoms", content="happy blossoms", catagory="oth")

        expected_data = [
            {
                "id": 1,
                "title": "blossoms",
                "thumbnail_pic": None,
                "rating": 0.0,
                "catagory": "oth",
                "read_time": 0,
            },
            {
                "id": 2,
                "title": "two blossoms",
                "thumbnail_pic": None,
                "rating": 0.0,
                "catagory": "oth",
                "read_time": 0,
            },
            {
                "id": 3,
                "title": "three blossoms",
                "thumbnail_pic": None,
                "rating": 0.0,
                "catagory": "oth",
                "read_time": 0,
            },
        ]
        expected_data = json.dumps(expected_data)
        response = client.get("/literature/catagories/poems/")
        self.assertJSONEqual(response.content, expected_data)

    @pytest.mark.django_db
    def test_stories_view(self):
        client = Client()

        jack = HemontikaUser.objects.get(pk=1)
        john = HemontikaUser.objects.get(pk=2)

        Story.objects.create(author=jack, title="a story about serializer", content="hello all", catagory="oth")
        Story.objects.create(author=jack, title="title", content="sharlock homes", catagory="oth")
        Story.objects.create(author=john, title="A man with a twisted lip", content="bla bla bla", catagory="oth")

        expected_data = [
            {
                "id": 1,
                "title": "a story about serializer",
                "thumbnail_pic": None,
                "rating": 0.0,
                "catagory": "oth",
                "read_time": 0,
            },
            {
                "id": 2,
                "title": "title",
                "thumbnail_pic": None,
                "rating": 0.0,
                "catagory": "oth",
                "read_time": 0,
            },
            {
                "id": 3,
                "title": "A man with a twisted lip",
                "thumbnail_pic": None,
                "rating": 0.0,
                "catagory": "oth",
                "read_time": 0,
            },
        ]

        expected_data = json.dumps(expected_data)
        response = client.get("/literature/catagories/stories/")
        self.assertJSONEqual(response.content, expected_data)

    @pytest.mark.django_db
    def test_books_view(self):
        client = Client()
        jack = HemontikaUser.objects.get(pk=1)
        novel = Novel.objects.create(author=jack, title="A novel about testing")

        poem1 = Poem.objects.create(author=jack, title="blossoms", content="hello blossoms")
        poem2 = Poem.objects.create(author=jack, title="two blossoms", content="happy blossoms")
        story = Story.objects.create(author=jack, title="a story about serializer", content="hello all")

        book = DragDropSelectBook.objects.create(author=jack, title=" a book about testing", catagory="oth")
        book.add_contents([novel, poem1, poem2, story])

        expected_data = [
            {
                "id": 1,
                "title": " a book about testing",
                "thumbnail_pic": None,
                "number_of_contents": 4,
                "rating": 0.0,
                "catagory": "oth",
            }
        ]

        expected_data = json.dumps(expected_data)
        response = client.get("/literature/catagories/books/")
        self.assertJSONEqual(response.content, expected_data)
