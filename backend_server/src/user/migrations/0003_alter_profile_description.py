# Generated by Django 3.2 on 2021-08-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_profile_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
