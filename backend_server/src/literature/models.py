from django.db import models
from tag.models import Tag
from hemontika_api import LANGUAGE_CHOICES, CATAGORY_CHOICES
from django.conf import settings

# Create your models here.


def unique_file_path(instance, filename):
    return "literature/{}/_{}_{}".format(type(instance).__name__, instance.author.id, filename)


class PreLiterature(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail_pic = models.ImageField(upload_to=unique_file_path, blank=True, null=True)

    class Meta:
        abstract = True


class Literature(PreLiterature):
    # basic fields for every literature
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    description = models.CharField(max_length=300)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=50)
    catagory = models.CharField(choices=CATAGORY_CHOICES, max_length=50)
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)

    def delete(self, *args, **kwargs):
        all_related_books = self.dragdropselectbook_set.all() if hasattr(self, "dragdropselectbook_set") else None
        if all_related_books:
            super().delete(*args, **kwargs)
            for book in list(all_related_books):
                book.set_number_of_contents()
        else:
            return super().delete(*args, **kwargs)

    class Meta:
        abstract = True


class ShortLiterature(Literature):
    content = models.TextField()
    read_time = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    class Meta:
        abstract = True


class Story(ShortLiterature):

    class Meta:
        verbose_name_plural = "Stories"


class Poem(ShortLiterature):
    pass


class Novel(Literature):
    number_of_chapters = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def create_chapter(self, content, part=None):

        # see if user provide a value for part argument and see whether the value is vaild or not
        try:
            chapter = None
            if content:
                count = self.chapter_set.count()
                if part is not None and count >= part - 1:
                    previous_chapter = self.chapter_set.all()[part - 1]
                    next_chapter = previous_chapter.next_chapter
                    chapter = Chapter(content=content, novel=self)
                    chapter.save()
                    chapter.previous_chapter = previous_chapter
                    chapter.save()
                    next_chapter.previous_chapter = chapter
                    next_chapter.save()
                    previous_chapter.save()
                #  if part is not given then add the new chapter to the last of the novel
                if not part:
                    super().save()
                    chapter = Chapter(content=content, novel=self)
                    chapter.save()
                    count = count + 1
                    if count > 1:
                        previous_chapter = self.chapter_set.all().order_by("-id")[1]

                        chapter.previous_chapter = previous_chapter
                        chapter.save()
            else:
                raise ValueError("No content provided")

        except ValueError as e:
            raise e
        except Exception as e:
            raise e
            # return "something went wrong"

        else:
            super().save()
            self.set_number_of_chapters()
            return chapter

    def set_number_of_chapters(self):
        chapters_count = self.chapter_set.count()
        self.number_of_chapters = chapters_count
        self.save()


class Chapter(PreLiterature):
    content = models.TextField()
    previous_chapter = models.OneToOneField(
        "self", models.SET_NULL, default=None, null=True, blank=True, related_name="next_chapter"
    )
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, blank=True)

    def delete(self, *args, **kwargs):
        novel = self.novel
        previous_chapter = self.previous_chapter
        next_chapter = self.next_chapter
        super().delete(*args, **kwargs)
        next_chapter.previous_chapter = previous_chapter
        next_chapter.save()
        novel.set_number_of_chapters()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.front_img = self.novel.front_img if self.front_img is not None else self.front_img
        # FIXME: the below code for setting `title` value is inefficient. Implement an efficient code instead
        if self.novel.chapter_set.count() > 1:
            chapters = list(self.novel.chapter_set.all())
            for index, chapter in enumerate(chapters):
                if self.id == chapter.id:
                    part_no = index + 1
                    self.title = self.novel.title + " Part- " + str(part_no)
        else:
            self.title = self.novel.title + " Part- 1"
        if self.tags.count() == 0 and self.novel.tags.count() > 0:
            for tag in self.novel.tags.all():
                tag.chapter_set.add(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["updated_at"]


class DragDropSelectBook(Literature):
    number_of_contents = models.PositiveIntegerField(default=0)
    novels = models.ManyToManyField(Novel, blank=True)
    stories = models.ManyToManyField(Story, blank=True)
    poems = models.ManyToManyField(Poem, blank=True)

    def add_contents(self, content_list):
        try:
            if content_list:
                for content in content_list:
                    if isinstance(content, Story):
                        self.stories.add(content)
                    elif isinstance(content, Poem):
                        self.poems.add(content)
                    elif isinstance(content, Novel):
                        self.novels.add(content)

                super().save()
                self.set_number_of_contents()

        except:
            raise Exception("Something went wrong")

    def set_number_of_contents(self):
        number_of_contents = 0
        stories_count, poems_count, novels_count = self.stories.count(), self.poems.count(), self.novels.count()
        if stories_count and stories_count > 0:
            number_of_contents += stories_count
        if poems_count and poems_count > 0:
            number_of_contents += poems_count
        if novels_count and novels_count > 0:
            number_of_contents += novels_count
        self.number_of_contents = number_of_contents
        self.save()

    def __str__(self):
        return self.title


# class ScratchBook(Literature):
#     content = models.TextField()
#     # TODO: we have to add chapter field also.