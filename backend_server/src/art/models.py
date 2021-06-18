from django.db import models
from literature.models import HemontikaUser
from tag.models import Tag

# Create your models here.


def unique_art_image(instance, filename):
    return "images/arts/_{}_{}".format(instance.artist.id, filename)


class Art(models.Model):
    artist = models.ForeignKey(HemontikaUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=unique_art_image)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
