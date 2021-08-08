from django.contrib.auth import get_user_model
from literature.models import Story, Poem, Book, Novel
from tag.models import Tag
from django.test import TestCase, Client
import pytest
import json
from freezegun import freeze_time

HemontikaUser = get_user_model()


@freeze_time("2021-01-01 11:12:13.000000")
class TestViews(TestCase):
    """tests for views"""

    DATE = "2021-01-01T11:12:13Z"

    @pytest.mark.django_db
    def test_novels_view(self):
        client = Client()

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
        novel2.create_chapter(content="testing novel view")
        novel2.create_chapter(content="hello novel")

        expected_data = [
            {
                "id": 1,
                "title": "A novel NOT about testing",
                "author": 1,
                # "front_img": "http://127.0.0.1:8000/front_img.png",
                "front_img": None,
                "date": self.DATE,
                "tags": [
                    1,
                ],
                "number_of_chapters": 2,
            },
            {
                "id": 2,
                "title": "Another novel",
                "author": 2,
                "front_img": None,
                "date": self.DATE,
                "tags": [],
                "number_of_chapters": 3,
            },
        ]
        expected_data = json.dumps(expected_data)
        response = client.get("/literature/novels/", HTTP_ACCEPT="application/json")
        self.assertJSONEqual(response.content, expected_data)

    @pytest.mark.django_db
    def test_poems_view(self):
        client = Client()

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

        expected_data = [
            {
                "id": 1,
                "title": "blossoms",
                "author": 1,
                "front_img": None,
                "date": self.DATE,
                "tags": [
                    1,
                ],
            },
            {
                "id": 2,
                "title": "two blossoms",
                "author": 2,
                "front_img": None,
                "date": self.DATE,
                "tags": [],
            },
            {
                "id": 3,
                "title": "three blossoms",
                "author": 2,
                "front_img": None,
                "date": self.DATE,
                "tags": [],
            },
        ]
        expected_data = json.dumps(expected_data)
        response = client.get("/literature/poems/")
        self.assertJSONEqual(response.content, expected_data)

    @pytest.mark.django_db
    def test_stories_view(self):
        client = Client()

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

        expected_data = [
            {
                "id": 1,
                "title": "a story about serializer",
                "author": 1,
                "front_img": None,
                "date": self.DATE,
                "tags": [
                    1,
                    2,
                    3,
                ],
            },
            {
                "id": 2,
                "title": "title",
                "author": 1,
                "front_img": None,
                "date": self.DATE,
                "tags": [
                    1,
                ],
            },
            {
                "id": 3,
                "title": "A man with a twisted lip",
                "author": 2,
                "front_img": None,
                "date": self.DATE,
                "tags": [],
            },
        ]

        expected_data = json.dumps(expected_data)
        response = client.get("/literature/stories/")
        self.assertJSONEqual(response.content, expected_data)

    @pytest.mark.django_db
    def test_books_view(self):
        client = Client()
        jack = HemontikaUser.objects.create(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )

        novel = Novel.objects.create(author=jack, title="A novel about testing")

        poem1 = Poem.objects.create(author=jack, title="blossoms", content="hello blossoms")
        poem2 = Poem.objects.create(author=jack, title="two blossoms", content="happy blossoms")
        story = Story.objects.create(author=jack, title="a story about serializer", content="hello all")

        book = Book.objects.create(author=jack, title=" a book about testing")
        book.add_contents([novel, poem1, poem2, story])

        expected_data = [
            {
                "id": 1,
                "title": " a book about testing",
                "author": 1,
                "front_img": None,
                "number_of_contents": 4,
                "date": self.DATE,
                "tags": [],
            }
        ]

        expected_data = json.dumps(expected_data)
        response = client.get("/literature/books/")
        self.assertJSONEqual(response.content, expected_data)
