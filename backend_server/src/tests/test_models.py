from api_app.models import HemontikaUser, Story, Poem, Book, Novel, Chapter
from django.test import TestCase
from django.db import transaction
import pytest

# Create your tests here.
# we prefer test driven development. So please write tests first before fixing any bug or adding any feature


class TestModels(TestCase):

    # @pytest.mark.django_db
    # def setUp(self):
    #     jack = HemontikaUser(username= 'karli56',first_name = 'jack', last_name= 'ma',email = 'jackma12@gmail.com', password = "kaka@134")
    #     jack.save()

    @pytest.mark.django_db
    def test_stories(self):
        jack = HemontikaUser(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        jack.save()
        content = "Is anything special needed for our project? may be."
        story = Story(author=jack, title="Anything special ..", content=content)
        story.save()
        assert story.author is not None
        assert story.title != ""
        assert story.content != ""

        with transaction.atomic():
            story2 = Story(title="Anthing special for me..", content=content)
            self.assertRaises(Exception, story2.save)
            story2 = Story()
            self.assertRaises(Exception, story2.save)
            story2 = Story(author=jack, content=content)
            self.assertRaises(Exception, story2.save)
        assert Story.objects.count() == 1

    @pytest.mark.django_db
    def test_poems(self):
        jack = HemontikaUser(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        jack.save()
        content = "Is anything special needed for our project? may be."
        poem = Poem(author=jack, title="Anything special ..", content=content)
        poem.save()
        assert poem.author is not None
        assert poem.title != ""
        assert poem.content != ""
        with transaction.atomic():
            poem2 = Poem(title="Anthing special for me..", content=content)
            self.assertRaises(Exception, poem2.save)
            poem2 = Poem()
            self.assertRaises(Exception, poem2.save)
            poem2 = Poem(author=jack, content=content)
            self.assertRaises(Exception, poem2.save)
        assert Poem.objects.count() == 1

    @pytest.mark.django_db
    def test_novels(self):
        jack = HemontikaUser(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        jack.save()
        novel = Novel(author=jack, title="A novel about testing")
        novel.save()
        novel.create_chapter(content="somthing here...")
        novel.create_chapter(content="somthing here too ...")
        novel.create_chapter(content="somthing here also ...")
        # print(chapter)
        assert Novel.objects.count() == 1
        assert novel.chapter_set.count() == 3
        assert Chapter.objects.count() == 3
        assert novel.number_of_chapters == 3
        assert novel.chapter_set.filter(content="").count() == 0
        assert novel.chapter_set.get(id=1).previous_chapter is None
        assert novel.chapter_set.get(id=1).title == "A novel about testing Part- 1"
        assert novel.chapter_set.get(id=1).next_chapter == novel.chapter_set.get(id=2)
        chapter_not_exist = False
        try:
            non_existing_chapter = novel.chapter_set.get(id=3).next_chapter  # noqa: F841
        except novel.chapter_set.get(id=3).DoesNotExist:
            chapter_not_exist = True
        self.assertEqual(chapter_not_exist, True)
        assert novel.chapter_set.get(id=3).previous_chapter == novel.chapter_set.get(id=2)
        chapter = novel.chapter_set.get(id=2)
        chapter.delete()
        assert novel.number_of_chapters == 2
        assert novel.chapter_set.get(id=1).next_chapter == novel.chapter_set.get(id=3)

    @pytest.mark.django_db
    def test_books(self):
        jack = HemontikaUser(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        jack.save()
        book = Book(author=jack, title=" a book about testing")
        story1 = Story.objects.create(
            author=jack, title="Anything special ..", content="hello all welcome to hemontika"
        )
        story2 = Story.objects.create(author=jack, title="Anything special ..", content="hello all again ..")
        story3 = Story.objects.create(author=jack, title="Anything special ..", content="filmstars are drunkers")
        poem = Poem.objects.create(author=jack, title="just testing", content="this is it.")
        novel = Novel(author=jack, title="a novel about testing")
        novel.create_chapter(content="hello my first chapter")
        novel.save()
        book.save()
        book.add_contents([story1, story2, story3, poem, novel])
        assert Book.objects.count() == 1
        assert book.number_of_contents == 5
        assert book.stories.count() == 3
        assert book.poems.get(id=1) == poem
        assert novel == book.novels.get(id=1)
        story3.delete()
        book = Book.objects.get(id=1)
        assert book.number_of_contents == 4
        novel.delete()
        book = Book.objects.get(id=1)
        assert book.number_of_contents == 3
        poem.delete()
        book = Book.objects.get(id=1)
        assert book.number_of_contents == 2
        # book2 = Book(author=jack,title='another book')
        # self.assertRaises(Exception,book.save)

    # @pytest.mark.django_db
    # def test_libraries(self):
