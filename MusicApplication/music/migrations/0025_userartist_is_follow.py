# Generated by Django 4.2.5 on 2023-10-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0024_remove_userartist_is_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='userartist',
            name='is_follow',
            field=models.BooleanField(default=False),
        ),
    ]
