# Generated by Django 4.2.5 on 2023-09-27 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_genre_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Lyric',
                'verbose_name_plural': 'Lyrics',
                'db_table': 'lyric',
                'managed': True,
            },
        ),
    ]
