from django.db import models
from literature.models import HemontikaUser
from tag.models import Tag

# Create your models here.


def unique_front_img(instance, filename):
    return "images/recitations/_{}_{}".format(instance.reciter.id, filename)


def unique_recitation_audio(instance, filename):
    return "videos/recitations/_{}_{}".format(instance.reciter.id, filename)


class Recitation(models.Model):
    reciter = models.ForeignKey(HemontikaUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    front_img = models.ImageField(upload_to=unique_front_img, null=True, blank=True)
    recitation_audio = models.FileField(upload_to=unique_recitation_audio)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
