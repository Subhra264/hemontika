from django.db import models
from tag.models import Tag
from hemontika_api.utils import REGION_CHOICES, COUNTRY_CHOICES, DISTRICT_CHOICES
from django.conf import settings

# Create your models here.


def unique_art_image(instance, filename):
    return "images/arts/_{}_{}".format(instance.artist.id, filename)


class Art(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=unique_art_image)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    rating = models.FloatField(default=0.0)
    views = models.PositiveBigIntegerField(default=0)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, null=True, blank=True)
    region = models.CharField(max_length=50, choices=REGION_CHOICES, blank=True, null=True)
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES, blank=True, null=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title
