# Generated by Django 3.2 on 2021-06-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tag", "0001_initial"),
        ("art", "0002_alter_art_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="art",
            name="tags",
            field=models.ManyToManyField(blank=True, to="tag.Tag"),
        ),
    ]
