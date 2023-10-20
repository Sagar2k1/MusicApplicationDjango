# Generated by Django 4.2.5 on 2023-10-13 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0022_track_top_trend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='is_follow',
        ),
        migrations.CreateModel(
            name='UserArtist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_follow', models.BooleanField(default=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserArtist',
                'verbose_name_plural': 'UserArtists',
                'db_table': 'user_artist',
                'managed': True,
            },
        ),
    ]