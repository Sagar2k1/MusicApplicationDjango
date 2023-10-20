from typing import Any
from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

# Create your models here.

def upload_to(instance, filename):
    return f'static/{instance.name}/{filename}'

class Area(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='khu-vuc/', default='khu-vuc/music_disc.jpg')
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'area'
        managed = True
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

class Genre(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='the-loai/', default='the-loai/music_disc.jpg')
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    slug = models.SlugField(null=True, unique=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        db_table = 'genre'
        managed = True
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='nghe-si/', default='nghe-si/music_disc.jpg')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)    
    follows = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name

    def follow(self, state:bool):
        if state:
            self.follows-=1
        else:
            self.follows+=1
        self.save()
        
    class Meta:
        db_table = 'artist'
        managed = True
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

class UserArtist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    is_follow = models.BooleanField(default=False)
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    
    def follow(self):
        if self.is_follow == True:
            self.is_follow = False
        else:
            self.is_follow = True
        
    class Meta:
        db_table = 'user_artist'
        managed = True
        verbose_name = 'UserArtist'
        verbose_name_plural = 'UserArtists'

        


class Lyric(models.Model):
    name = models.CharField(max_length=100,null=True)
    content = models.TextField()    

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'lyric'
        managed = True
        verbose_name = 'Lyric'
        verbose_name_plural = 'Lyrics'

class Track(models.Model):
    name = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    artists = models.ManyToManyField(Artist)
    lyrics = models.ManyToManyField(Lyric, null=True)
    file = models.URLField(max_length=200, default='https://www.youtube.com/watch?v=Ora2P-xjPgA')
    image = models.ImageField(upload_to='bai-hat/',default='bai-hat/music_disc.jpg')
    favorites = models.IntegerField(default=0)
    streams = models.IntegerField(default=0)
    top_trend = models.IntegerField(default=-1)
    is_trend = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, unique=True)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def increase_stream(self):
        self.streams+=1
        self.save()
    
    def set_trend(self):
        if self.is_trend:
            self.is_trend=False
        else:
            self.is_trend=True
        self.save()
    
    def set_top(self,top: int):
        self.top_trend = top
    
    class Meta:
        db_table = 'track'
        verbose_name = "Track"
        verbose_name_plural = "Tracks"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Track_detail", kwargs={"pk": self.pk})
'''
class Trend(models.Model):
    top = models.BigIntegerField(primary_key=True,auto_created=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'trend'
        managed = True
        verbose_name = 'Trend'
        verbose_name_plural = 'Trends'
'''

class Album(models.Model):
    name = models.CharField(max_length=100)
    tracks = models.ManyToManyField(Track)
    artists = models.ManyToManyField(Artist, null= True)
    image = models.ImageField(upload_to='album/', default='album/music_disc.jpg')
    favorites = models.IntegerField(default=0)
    streams = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def increase_stream(self):
        self.streams+=1
        self.save()
        
    def __str__(self) -> str:
        return self.name
            
    class Meta:
        db_table = 'album'
        verbose_name = "Album"
        verbose_name_plural = "Albums"

def set_trend_track():
    track = Track.objects.all().order_by('-streams')
    top = 100
    if track.__len__()>top:
        for i in range(len(track)):
            if i<100 :
                if not track[i].is_trend:
                    track[i].set_trend()
            else:
                if track[i].is_trend:
                    track[i].set_trend()
            track[i].set_top(i+1)
    else:
        for i in range(track.__len__()):
            if not track[i].is_trend:
                track[i].set_trend()
            track[i].set_top(i)
                
    