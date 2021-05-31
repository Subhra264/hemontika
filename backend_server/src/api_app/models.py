from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class HemontikaUser(User):
    """This class extends the User model. It have various foreign key to other models so that user can
    access the full feature of those models.
    """

    pass


# have to move the tag class to the Tag_api app
class Tag(models.Model):
    name = models.CharField(max_length=60)


class Literature(models.Model):
    # basic fields for every literature
    author = models.ForeignKey(HemontikaUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    front_img = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def delete(self, *args, **kwargs):
        all_related_books = self.book_set.all() if hasattr(self, 'book_set') else None
        if all_related_books:
            super().delete(*args, **kwargs)
            for book in list(all_related_books):
                book.set_number_of_contents()
        else:
            return super().delete(*args, **kwargs)

    class Meta:
        abstract = True


class Story(Literature):
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Stories"


class Poem(Literature):
    content = models.TextField()

    def __str__(self):
        return self.title


class Novel(Literature):
    number_of_chapters = models.PositiveIntegerField(default=0)

    # def save(self,*args, **kwargs):
    #     if self.chapter_set.count() == 0:
    #         return

    def __str__(self):
        return self.title

    def create_chapter(self, content, part=None):

        # see if user provide a value for part argument and see whether the value is vaild or not
        try:
            chapter = None
            if content:
                # count = Chapter.objects.filter(novel=self).count()
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


class Chapter(Literature):
    author = models.ForeignKey(HemontikaUser, on_delete=models.CASCADE, blank=True, null=True)
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
        self.front_img = self.novel.front_img if self.front_img is None else self.front_img
        # FIXME: the below code for setting `title` value is inefficient. Implement an efficient code instead
        if self.novel.chapter_set.count() > 1:
            chapters = list(self.novel.chapter_set.all())
            for index, chapter in enumerate(chapters):
                if self.id == chapter.id:
                    part_no = index + 1
                    self.title = self.novel.title + " Part- " + str(part_no)
        else:
            self.title = self.novel.title + " Part- 1"

        if not self.author:
            self.author = self.novel.author
        if self.tags is None and self.novel.tags.count() > 0:
            self.tags.set(self.novel.tags)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]


class Book(Literature):
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

    # def save(self,*args,**kwargs):
    #     if self.number_of_contents > 0:
    #         super().save(*args,**kwargs)
    #     else:
    #         raise Exception('no content provided')

    def __str__(self):
        return self.title
