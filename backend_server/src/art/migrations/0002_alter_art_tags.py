# Generated by Django 3.2 on 2021-06-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tag", "0001_initial"),
        ("art", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="art",
            name="tags",
            field=models.ManyToManyField(blank=True, null=True, to="tag.Tag"),
        ),
    ]
