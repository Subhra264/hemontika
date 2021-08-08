# Generated by Django 3.2 on 2021-08-07 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("music", "0004_alter_music_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="music",
            name="musician",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
