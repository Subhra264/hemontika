# Generated by Django 3.2 on 2021-06-11 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("literature", "0001_initial"),
        ("tag", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Music",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=50)),
                ("video", models.FileField(blank=True, upload_to="")),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "musician",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="literature.hemontikauser"),
                ),
                ("tags", models.ManyToManyField(blank=True, null=True, to="tag.Tag")),
            ],
        ),
    ]
