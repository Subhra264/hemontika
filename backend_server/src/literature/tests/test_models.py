from literature.models import Story, Poem, DragDropSelectBook, Novel, Chapter
from tag.models import Tag
from django.contrib.auth import get_user_model
from tempfile import NamedTemporaryFile
from django.core.files import File
from django.test import TestCase
from django.db import transaction
import pytest

# Create your tests here.
# we prefer test driven development. So please write tests first before fixing any bug or adding any feature
HemontikaUser = get_user_model()


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="horror")
        Tag.objects.create(name="adventure")
        Tag.objects.create(name="mystry")
        Tag.objects.create(name="comedy")
        Tag.objects.create(name="sci-fi")

    @pytest.mark.django_db
    def test_stories(self):
        jack = HemontikaUser(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@gmail.com", password="kaka@134"
        )
        jack.save()
        content = "Is anything special needed for our project? may be."
        story = Story.objects.create(author=jack, title="Anything special ..", content=content)
        story.save()
        tag = Tag.objects.get(id=1)
        tag.story_set.add(story)
        Tag.objects.get(id=3).story_set.add(story)
        assert story.author is not None
        assert story.title != ""
        assert story.content != ""
        self.assertEqual(story.tags.count(), 2)
        self.assertEqual(story.tags.get(id=1), tag)
        self.assertEqual(story.tags.get(id=3), Tag.objects.get(id=3))
        self.assertEqual(story.read_time, 0)
        self.assertEqual(story.rating, 0.0)
        # TODO: have to images as well as created_at, updated_at etc.

        with transaction.atomic():
            story2 = Story(title="Anthing special for me..", content=content)
            self.assertRaises(Exception, story2.save)
            story2 = Story()
            self.assertRaises(Exception, story2.save)
            story2 = Story(title="Another special for me", author=jack, content=content)
            self.assertRaises(Exception, story2.save)
            story2 = Story(
                title="anything special for me..", content=content, author=jack, description="hello description"
            )
            self.assertRaises(Exception, story2.save)
            story2 = Story(
                title="anything special for me..",
                content=content,
                author=jack,
                description="hello description",
                language="en",
            )
            story2 = Story(author=jack, content=content)
            self.assertRaises(Exception, story2.save)
        assert Story.objects.count() == 1

    @pytest.mark.django_db
    def test_poems(self):
        jack = HemontikaUser(
            username="karli56", first_name="jack", last_name="ma", email="jackma12@email.com", password="kaka@134"
        )
        jack.save()
        content = "Is anything special needed for our project? may be."
        poem = Poem(author=jack, title="Anything special ..", content=content)
        poem.save()
        tag = Tag.objects.get(id=1)
        tag.poem_set.add(poem)
        self.assertEqual(poem.tags.count(), 1)
        self.assertEqual(poem.tags.get(id=1), tag)
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
            username="karli56", first_name="jack", last_name="ma", email="jackma12@email.com", password="kaka@134"
        )
        jack.save()
        novel = Novel(author=jack, title="A novel about testing")
        temp_img = File(NamedTemporaryFile(suffix="jpg"))
        temp_img.name = "test_image.jpg"
        novel.thumbnail_pic = temp_img
        novel.save()
        Tag.objects.get(id=4).novel_set.add(novel)
        Tag.objects.get(id=5).novel_set.add(novel)
        Tag.objects.get(id=2).novel_set.add(novel)
        chapter1 = novel.create_chapter(content="somthing here...")
        chapter2 = novel.create_chapter(content="somthing here too ...")
        novel.create_chapter(content="somthing here also ...")
        self.assertRegex(novel.thumbnail_pic.name, r"literature/Novel/_1_test_image()|(_([0-9a-zA-Z]){7}).jpg")
        self.assertEqual(novel.tags.count(), 3)
        self.assertEqual(novel.tags.get(id=4), Tag.objects.get(id=4))
        self.assertRegex(chapter1.thumbnail_pic.name, r"literature/Novel/_1_test_image()|(_([0-9a-zA-Z]){7}).jpg")
        self.assertRegex(chapter2.thumbnail_pic.name, r"literature/Novel/_1_test_image()|(_([0-9a-zA-Z]){7}).jpg")
        assert Novel.objects.count() == 1
        assert novel.chapter_set.count() == 3
        assert Chapter.objects.count() == 3
        assert novel.number_of_chapters == 3
        assert novel.chapter_set.filter(content="").count() == 0
        assert chapter1.previous_chapter is None
        assert chapter1.title == "A novel about testing Part- 1"
        assert chapter1.next_chapter == novel.chapter_set.get(id=2)
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
        book = DragDropSelectBook(author=jack, title=" a book about testing")
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
        assert DragDropSelectBook.objects.count() == 1
        assert book.number_of_contents == 5
        assert book.stories.count() == 3
        assert book.poems.get(id=1) == poem
        assert novel == book.novels.get(id=1)
        story3.delete()
        book = DragDropSelectBook.objects.get(id=1)
        assert book.number_of_contents == 4
        novel.delete()
        book = DragDropSelectBook.objects.get(id=1)
        assert book.number_of_contents == 3
        poem.delete()
        book = DragDropSelectBook.objects.get(id=1)
        assert book.number_of_contents == 2
        # book2 = Book(author=jack,title='another book')
        # self.assertRaises(Exception,book.save)

    # @pytest.mark.django_db
    # def test_libraries(self):
