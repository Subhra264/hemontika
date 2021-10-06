# Generated by Django 3.2 on 2021-09-30 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recitation", "0004_alter_recitation_reciter"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recitation",
            old_name="front_img",
            new_name="thumbnail_pic",
        ),
        migrations.AddField(
            model_name="recitation",
            name="description",
            field=models.CharField(default="this is the description", max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="recitation",
            name="language",
            field=models.CharField(
                choices=[
                    ("asm", "Assamese"),
                    ("bn", "Bengali"),
                    ("en", "English"),
                    ("gu", "Gujarati"),
                    ("hi", "Hindi"),
                    ("kha", "Khasi"),
                    ("kn", "Kannada"),
                    ("kok", "Konkani"),
                    ("lus", "Lushai"),
                    ("ml", "Malayalam"),
                    ("mr", "Marathi"),
                    ("mni", "Meitei"),
                    ("nep", "Nepali"),
                    ("nls", "Not_lang_spec"),
                    ("ori", "Oriya"),
                    ("pan", "Panjabi"),
                    ("ta", "Tamil"),
                    ("te", "Telugu"),
                    ("ur", "Urdu"),
                ],
                default="bn",
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="recitation",
            name="rating",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="recitation",
            name="views",
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]