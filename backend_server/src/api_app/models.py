from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class HemontikaUser(User):
    """ This class extends the User model. It have various foreign key to other models so that user can 
        access the full feature of those models.
    """
    pass


class Tag(models.Model):
    name = models.CharField(max_length=60)

class Literature(models.Model):
    # basic fields for every literature
    author = models.ForeignKey(HemontikaUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    front_img = models.ImageField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add= True)
    tags = models.ManyToManyField(Tag,blank=True)

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
    
    def create_chapter(self,content,part=None):

        # see if user provide a value for part argument and see whether the value is vaild or not
        try:
            chapter = None
            if content:
                # count = Chapter.objects.filter(novel=self).count()
                count = self.chapter_set.count()
                if part is not None and count >= part - 1:
                    previous_chapter = self.chapter_set.all()[part - 1]
                    next_chapter = previous_chapter.next_chapter
                    chapter = Chapter(content=content,novel = self)
                    chapter.save()
                    chapter.previous_chapter = previous_chapter
                    chapter.save()
                    next_chapter.previous_chapter = chapter
                    next_chapter.save()
                    previous_chapter.save()
                #  if part is not given then add the new chapter to the last of the novel
                if not part:
                    super().save()
                    chapter = Chapter(content=content,novel = self)
                    chapter.save()
                    count = count+1
                    if count > 1:
                        previous_chapter = self.chapter_set.all().order_by("-date")[1]

                        chapter.previous_chapter = previous_chapter
                        chapter.save()
            else:
                raise ValueError("No content provided")
                    
        except ValueError as e:
            raise e
        except Exception as e:
            return "something went wrong"
            
        else:
            self.number_of_chapters = self.number_of_chapters + 1
            super().save()
            return chapter


class Chapter(Literature):
    author = models.ForeignKey(HemontikaUser,on_delete=models.CASCADE,blank=True,null=True)
    content = models.TextField()
    previous_chapter = models.OneToOneField('self',models.SET_NULL,default=None,null=True,blank=True,related_name="next_chapter")
    novel = models.ForeignKey(Novel,on_delete=models.CASCADE,blank=True)

    def pre_delete(self,*args,**kwargs):
        previous_chapter = self.previous_chapter
        next_chapter = self.next_chapter
        next_chapter.previous_chapter = previous_chapter
        next_chapter.save()


    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        self.front_img = self.novel.front_img if self.front_img is None else self.front_img
        # FIXME: the below code for setting `title` value is inefficient. Implement an efficient code instead
        if self.novel.chapter_set.count() > 1:
            chapters = list(self.novel.chapter_set.all())
            print(chapters)
            for index,chapter in enumerate(chapters):
                print('printed time')
                print(chapter)
                print(self)
                if self.id == chapter.id:
                    print('self is found')
                    part_no = index+1
                    self.title = self.novel.title + ' Part- ' + str(part_no)
        else:
            self.title = self.novel.title + ' Part- 1'
        
        if not self.author:
            self.author = self.novel.author
        if self.tags is None and self.novel.tags.count() > 0:
            self.tags.set(self.novel.tags)
        super().save(*args,**kwargs)
        # print(self.title)

    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ["date"]


class Book(Literature):
    number_of_contents = models.PositiveIntegerField(default=0)
    novels = models.ManyToManyField(Novel,blank=True)
    stories = models.ManyToManyField(Story,blank=True)
    poems = models.ManyToManyField(Poem,blank=True)


    def add_contents(self,content_list):
        try:
            if content_list:
                for content in content_list:
                    if isinstance(content,Story):
                        self.stories.add(content)
                        self.number_of_contents = self.number_of_contents + 1
                    elif isinstance(content,Poem):
                        self.poems.add(content)
                        self.number_of_contents = self.number_of_contents + 1
                    elif isinstance(content,Novel):
                        self.novels.add(content)
                        self.number_of_contents = self.number_of_contents + 1
                
                super().save()
            
        except:
            raise Exception('Something went wrong')
    
    # def save(self,*args,**kwargs):
    #     if self.number_of_contents > 0:
    #         super().save(*args,**kwargs)
    #     else:
    #         raise Exception('no content provided')
    
    def __str__(self):
        return self.title
    

