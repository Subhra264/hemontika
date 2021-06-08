# Generated by Django 3.2 on 2021-05-03 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="story",
            options={"verbose_name_plural": "Stories"},
        ),
        migrations.RemoveField(
            model_name="chapter",
            name="next_chapter",
        ),
        migrations.AddField(
            model_name="book",
            name="front_img",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="chapter",
            name="front_img",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="novel",
            name="front_img",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="poem",
            name="front_img",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="story",
            name="front_img",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="book",
            name="tags",
            field=models.ManyToManyField(blank=True, to="api_app.Tag"),
        ),
        migrations.AlterField(
            model_name="chapter",
            name="author",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="api_app.hemontikauser"
            ),
        ),
        migrations.AlterField(
            model_name="chapter",
            name="novel",
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to="api_app.novel"),
        ),
        migrations.AlterField(
            model_name="chapter",
            name="previous_chapter",
            field=models.OneToOneField(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="next_chapter",
                to="api_app.chapter",
            ),
        ),
        migrations.AlterField(
            model_name="chapter",
            name="tags",
            field=models.ManyToManyField(blank=True, to="api_app.Tag"),
        ),
        migrations.AlterField(
            model_name="novel",
            name="tags",
            field=models.ManyToManyField(blank=True, to="api_app.Tag"),
        ),
        migrations.AlterField(
            model_name="poem",
            name="tags",
            field=models.ManyToManyField(blank=True, to="api_app.Tag"),
        ),
        migrations.AlterField(
            model_name="story",
            name="tags",
            field=models.ManyToManyField(blank=True, to="api_app.Tag"),
        ),
    ]
