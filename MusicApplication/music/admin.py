from django.contrib import admin
from .models import Track, Genre, Artist, Album, Lyric, Area

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name','area','description')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display=('name', 'favorites', 'streams', 'created_at')

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name','favorites', 'streams',)

@admin.register(Lyric)
class LyricAdmin(admin.ModelAdmin):
    list_display = ('name','content')
    

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name','image')
    

