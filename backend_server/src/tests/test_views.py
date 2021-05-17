from api_app.views import *
from api_app.models import *
from api_app.serializers import *
from django.test import TestCase
import pytest
import requests,json
from freezegun import freeze_time

@freeze_time("2021-01-01 11:12:13.000000")
class TestViews(TestCase):
    '''tests for views'''

    DATE = "2021-01-01T11:12:13Z"

    @pytest.mark.django_db
    def test_novels_view(self):
        Url = 'http://127.0.0.1:8000/api/novels/'

        jack = HemontikaUser.objects.create(username= 'karli56',first_name = 'jack', last_name= 'ma',email = 'jackma12@gmail.com', password = "kaka@134")
        john = HemontikaUser.objects.create(username= 'johni56',first_name = 'john', last_name= 'doe',email = 'johndoe12@gmail.com', password = "kaka@134")
        tag = Tag.objects.create(name='novel')
        novel = Novel.objects.create(author= jack, title = 'A novel NOT about testing')
        tag.novel_set.add(novel)
        novel.create_chapter(content='somthing here...')
        novel.create_chapter(content='somthing here too ...')

        novel2 = Novel.objects.create(author=john, title='Another novel')
        novel2.create_chapter(content='anything important')
        novel2.create_chapter(content='testing novel view')
        novel2.create_chapter(content='hello novel')
       
        expected_data = [{
                "id":1,
                "title":"A novel NOT about testing",
                "author": "http://127.0.0.1:8000/api/user/karli56/",
                "front_img": "http://127.0.0.1:8000/front_img.png",
                "date": self.DATE,
                "tags":[
                    "http://127.0.0.1:8000/api/tags/novel",
                ],
                "no_of_chapters":2,
                "chapters":[1,2],
            },
            {
                "id":2,
                "title":"Another novel",
                "author":"http://127.0.0.1:8000/api/user/johni56/",
                "front_img": "http://127.0.0.1:8000/front_img2.png",
                "date":self.DATE,
                "tags":[],
                "no_of_chapters":3,
                "chapters":[3,4,5]
            }
        ]
        expected_data = json.dumps(expected_data)
        response = requests.get(url=Url)
        self.assertJSONEqual(response.content, expected_data)


    @pytest.mark.django_db
    def test_poems_view(self):
        Url = 'http://127.0.0.1:8000/api/poems/'

        jack = HemontikaUser.objects.create(username= 'karli56',first_name = 'jack', last_name= 'ma',email = 'jackma12@gmail.com', password = "kaka@134")
        john = HemontikaUser.objects.create(username= 'johni56',first_name = 'john', last_name= 'doe',email = 'johndoe12@gmail.com', password = "kaka@134")
        tag = Tag.objects.create(name='poem')
        poem = Poem.objects.create(author=jack,title='blossoms', content=' beautiful blossoms')
        tag.poem_set.add(poem)
        Poem.objects.create(author=john,title='two blossoms', content='hello blossoms')
        Poem.objects.create(author=john,title='three blossoms',content='happy blossoms')

        expected_data = [{
                "id":1,
                "title":"blossoms",
                "author_url": "http://127.0.0.1:8000/api/user/karli56/",
                "content_url":"http://127.0.0.1:8000/api/poems/1/",
                "front_img": "http://127.0.0.1:8000/front_img.png",
                "date": self.DATE,
                "tags":[
                    "http://127.0.0.1:8000/api/tags/poem",
                ],

            },
            {
                "id":2,
                "title":"two blossoms",
                "author":"http://127.0.0.1:8000/api/user/johni56/",
                "content_url": "http:// 127.0.0.1:8000/api/poems/2/",
                "front_img": "http://127.0.0.1:8000/front_img.png",
                "date": self.DATE,
                "tags":[],
            },
            {
                "id":3,
                "title":"three blossoms",
                "author":"http://127.0.0.1:8000/api/user/johni56/",
                "content_url": "http:// 127.0.0.1:8000/api/poems/3/",
                "front_img": "http://127.0.0.1:8000/front_img.png",
                "date": self.DATE,
                "tags":[],
            }
        ]
        expected_data = json.dumps(expected_data)
        response = requests.get(url=Url)
        self.assertJSONEqual(response.content, expected_data)



    @pytest.mark.django_db
    def test_stories_view(self):
        Url = 'http://127.0.0.1:8000/api/stories/'

        jack = HemontikaUser.objects.create(username= 'karli56',first_name = 'jack', last_name= 'ma',email = 'jackma12@gmail.com', password = "kaka@134")
        john = HemontikaUser.objects.create(username= 'johni56',first_name = 'john', last_name= 'doe',email = 'johndoe12@gmail.com', password = "kaka@134")
        tag = Tag.objects.create(name='horror')
        tag2 = Tag.objects.create(name='bengali')
        tag3 = Tag.objects.create(name='short stories')

        story = Story.objects.create(author=jack,title='a story about serializer',content='hello all')
        story2 = Story.objects.create(author=jack,title='title',content='sharlock homes')
        stroy3 = Story.objects.create(author=john,title='A man with a twisted lip', content='bla bla bla')
        tag.story_set.set([story,story2])
        tag2.story_set.add(story)
        tag3.story_set.add(story)

        expected_data = [{
                "id":1,
                "title":"a story about serializer",
                "author_url": "http://127.0.0.1:8000/api/user/karli56/",
                "content_url":"http://127.0.0.1:8000/api/stories/1/",
                "front_img": "http://127.0.0.1:8000/front_img.png",
                "date": self.DATE,
                "tags":[
                    "http://127.0.0.1:8000/api/tags/horror/",
                    "http://127.0.0.1:8000/api/tags/bengali/",
                    "http://127.0.0.1:8000/api/tags/short-stories"
                ],

            },
            {
                "id":2,
                "title":"title",
                "author":"http://127.0.0.1:8000/api/user/karli56/",
                "content_url": "http:// 127.0.0.1:8000/api/stories/2/",
                "front_img": "http://127.0.0.1:8000/front_img.png",
                "date": self.DATE,
                "tags":["http://127.0.0.1:8000/api/tags/horror/"],
            },
            {
                "id":3,
                "title":"A man with a twisted lip",
                "author":"http://127.0.0.1:8000/api/user/johni56/",
                "content_url": "http:// 127.0.0.1:8000/api/stories/2/",
                "front_img": "http://127.0.0.1:8000/front_img.png",
                "date": self.DATE,
                "tags":[],
            }

        ]

        expected_data = json.dumps(expected_data)
        response = requests.get(url=Url)
        self.assertJSONEqual(response.content, expected_data)



    @pytest.mark.django_db
    def test_books_view(self):
        Url = 'http://127.0.0.1:8000/api/books/'

        jack = HemontikaUser.objects.create(username= 'karli56',first_name = 'jack', last_name= 'ma',email = 'jackma12@gmail.com', password = "kaka@134")
        
        novel = Novel.objects.create(author= jack, title = 'A novel about testing')
        chapter1 = novel.create_chapter(content='hello chapter')
        chapter2 = novel.create_chapter(content='chapter 2')

        poem1 = Poem.objects.create(author=jack,title='blossoms', content='hello blossoms')
        poem2 = Poem.objects.create(author=jack,title='two blossoms', content='happy blossoms')
        story = Story.objects.create(author=jack,title='a story about serializer',content='hello all')

        book = Book.objects.create(author=jack,title=' a book about testing')
        book.add_contents([novel,poem1,poem2,story])

        expected_data = [{
                "id":1,
                "title":" a book about testing",
                "author":"http://127.0.0.1:8000/api/user/karli56/",
                "front_img": "http://127.0.0.1:8000/front_img.png",
                "date": self.DATE,
                "novels":[1,],
                "stories":[1,],
                "poems":[1,2],
                "tags":[],

            }
        ]

        expected_data = json.dumps(expected_data)
        response = requests.get(url=Url)
        self.assertJSONEqual(response.content, expected_data)


    def test_tags_view(self):
        Url = "http://127.0.0.1:8000/api/tags/"

        Tag.objects.create(name="horror")
        Tag.objects.create(name='mystry')
        Tag.objects.create(name='fiction')
        Tag.objects.create(name='crime')

        expected_data = [{
                "id":1,
                "name":"horror",
            },
            {
                "id":2,
                "name": "mystry"
            },
            {
                "id":3,
                "name":"fiction"
            },
            {
                "id":4,
                "name":"crime"
            }
        ]

        expected_data = json.dumps(expected_data)
        response = requests.get(url=Url)
        self.assertJSONEqual(response.content, expected_data)
        assert response.status_code == 200


    def test_tag_view(self):
        Url = "http://127.0.0.1:8000/api/tags/1/"

        Tag.objects.create(name="horror")
        Tag.objects.create(name='mystry')
        Tag.objects.create(name='fiction')
        Tag.objects.create(name='crime')

        expected_data = {
            "id":1,
            "name":"horror",
            "poems":[],
            "novels":[],
            "stories":[],
            "books":[]
        }
        expected_data = json.dumps(expected_data)
        response = requests.get(url=Url)
        self.assertJSONEqual(response.content, expected_data)