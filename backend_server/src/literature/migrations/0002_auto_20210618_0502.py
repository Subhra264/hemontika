# Generated by Django 3.2 on 2021-06-18 05:02

from django.db import migrations, models
import literature.models


class Migration(migrations.Migration):

    dependencies = [
        ("literature", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="front_img",
            field=models.ImageField(blank=True, null=True, upload_to=literature.models.unique_file_path),
        ),
        migrations.AlterField(
            model_name="chapter",
            name="front_img",
            field=models.ImageField(blank=True, null=True, upload_to=literature.models.unique_file_path),
        ),
        migrations.AlterField(
            model_name="novel",
            name="front_img",
            field=models.ImageField(blank=True, null=True, upload_to=literature.models.unique_file_path),
        ),
        migrations.AlterField(
            model_name="poem",
            name="front_img",
            field=models.ImageField(blank=True, null=True, upload_to=literature.models.unique_file_path),
        ),
        migrations.AlterField(
            model_name="story",
            name="front_img",
            field=models.ImageField(blank=True, null=True, upload_to=literature.models.unique_file_path),
        ),
    ]
