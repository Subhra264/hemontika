from django.db import models
from django.conf import settings


def unique_user_path(instance, filename):
    return "users/profiles/_{}_{}".format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to=unique_user_path)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username + " - profile"
