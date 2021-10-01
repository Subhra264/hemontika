from django.db import models
from tag.models import Tag
from hemontika_api import LANGUAGE_CHOICES
from hemontika_api.utils import COUNTRY_CHOICES, REGION_CHOICES, DISTRICT_CHOICES
from django.conf import settings

# create your models here


def unique_user_path(instance, filename):
    return "videos/musics/_{}_{}".format(instance.musician.id, filename)


class Music(models.Model):
    musician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to=unique_user_path)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    rating = models.FloatField(default=0.0)
    views = models.PositiveBigIntegerField(default=0)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, null=True, blank=True)
    region = models.CharField(max_length=50, choices=REGION_CHOICES, blank=True, null=True)
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES, blank=True, null=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title
