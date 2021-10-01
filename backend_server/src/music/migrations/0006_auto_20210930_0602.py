# Generated by Django 3.2 on 2021-09-30 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0005_alter_music_musician"),
    ]

    operations = [
        migrations.AddField(
            model_name="music",
            name="country",
            field=models.CharField(
                blank=True, choices=[("IN", "INDIA"), ("USA", "UNITED sTATES")], max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="music",
            name="description",
            field=models.CharField(default="this is the description", max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="music",
            name="district",
            field=models.CharField(
                blank=True, choices=[("HOW", "HOWRAH"), ("HOO", "HOOGLY"), ("KOL", "KOLKATA")], max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="music",
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
            model_name="music",
            name="rating",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="music",
            name="region",
            field=models.CharField(
                blank=True,
                choices=[("WB", "WEST BENGAL"), ("UP", "UTTAR PRADESH"), ("MP", "MADHYA PRADESH"), ("TN", "TAMILNADU")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="music",
            name="views",
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
