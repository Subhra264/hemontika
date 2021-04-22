from django.test import TestCase
import pytest
from unittest.mock import Mock,patch
from .models import *

# Create your tests here.
# we prefer test driven development. So please write tests first before fixing any bug or adding any feature

class TestModels(TestCase):

    @pytest.mark.django_db
    def setUp(self):
        jack = User(username= 'karli56',first_name = 'jack', last_name= 'ma',email = 'jackma12@gmail.com', password = "kaka@134")
        jack.save()

    # def test_user(self):
        
    #     pass
    
    @pytest.mark.django_db
    def test_stories(self):
        content = 'Is anything special needed for our project? may be.'
        story = Story(author = jack, title = 'Anything special ..', content = content)
        story.save()
        assert story.author is not None
        assert story.title != ''
        assert story.content != ''

        story2 = Story(title= 'Anthing special for me..', content= content)
        self.assertRaises(Exception, story2.save)
        story2 = Story()
        self.assertRaises(Exception,story2.save)
        story2 = Story(author = jack,content= content)
        self.assertRaises(Exception,story2.save)
        assert Story.objects.count() == 1

    @pytest.mark.django_db
    def test_poems(self):
        content = 'Is anything special needed for our project? may be.'
        poem = Poem(author = jack, title = 'Anything special ..', content = content)
        poem.save()
        assert poem.author is not None
        assert poem.title != ''
        assert poem.content != ''

        poem2 = Story(title= 'Anthing special for me..', content= content)
        self.assertRaises(Exception, poem2.save)
        poem2 = Poem()
        self.assertRaises(Exception,poem2.save)
        poem2 = Poem(author = jack,content= content)
        self.assertRaises(Exception,poem2.save)
        assert Poem.objects.count() == 1

    @pytest.mark.django_db
    def test_novels(self):
        novel = Novel(author= jack, title = 'A novel about testing')
        novel.create_chapters(content='somthing here...')
        novel.create_chapters(content='somthing here too ...')
        novel.create_chapters(content='somthing here also ...')
        novel.save()
        assert Novel.objects.count() == 1
        assert novel.number_of_chapters == 3
        assert novel.chapters.filter(content='') == 0
        assert novel.chapters.get(id=1).previous_chapter is None
        assert novel.chapters.get(id=1).next_chapter is novel.chapters.get(id=2)
        assert novel.chapters.get(id=3).next_chapter is None
        assert novel.chapters.get(id=3).previous_chapter is novel.chapters.get(id=2)

    @pytest.mark.django_db
    def test_books(self):
        book = Book(author=jack,title=' a book about testing')
        story1 = Story.objects.create(author = jack, title = 'Anything special ..', content = 'hello all welcome to hemontika')
        story2 = Story.objects.create(author = jack, title = 'Anything special ..', content = 'hello all again ..')
        story3 = Story.objects.create(author = jack, title = 'Anything special ..', content = 'filmstars are drunkers')
        book.add_story([story1,story2,story3])
        book.save()
        assert Book.objects.count() == 1
        assert book.no_of_stories == 3
        assert book.stories.get(id=1).previous_story is None
        assert book.stories.get(id=2).previous_story is book.stories.get(id=1)
        assert book.stories.get(id=3).next_story is None

    
    # @pytest.mark.django_db
    # def test_libraries(self):
        