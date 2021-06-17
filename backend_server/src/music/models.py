from django.db import models
from tag.models import Tag
from literature.models import HemontikaUser

# create your models here


class Music(models.Model):
    musician = models.ForeignKey(HemontikaUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    video = models.FileField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
