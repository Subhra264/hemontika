from django.db import models
from api_app.models import HemontikaUser
from tag.models import Tag

# Create your models here.


class Recitation(models.Model):
    reciter = models.ForeignKey(HemontikaUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    front_img = models.ImageField(blank=True)  # NOTE: front_img and audio should be necessary
    recitation_audio = models.FileField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
