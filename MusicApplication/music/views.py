from django.shortcuts import render, redirect
from .models import Track, Album, Artist, Genre, Area, Lyric, UserArtist
from django.shortcuts import get_object_or_404
from django.conf import settings
from slugify import slugify
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def genre_view(request):
    # album  
    album = Album.objects.all()
    album_vn = Album.objects.filter(tracks__genres__area__name = 'Việt Nam').distinct()
    album_hanquoc= Album.objects.filter(tracks__genres__area__name= 'Hàn Quốc').distinct()
    album_usuk= Album.objects.filter(tracks__genres__area__name= 'Âu Mỹ').distinct()
    
    # track
    if Track.objects.all().__len__()<10:
        tracks = Track.objects.all().order_by('streams')
    else:
        tracks = Track.objects.all().order_by('streams')[:10]
    # Tất cả thể loại việt nam
    genres_vn = Genre.objects.filter(area__name='Việt Nam').distinct()
    # Tất cả thể loại Hàn Quốc
    genres_hq = Genre.objects.filter(area__name='Hàn Quốc').distinct()
    # Tất cả thể loại Âu Mỹ
    genres_usuk = Genre.objects.filter(area__name='Âu Mỹ').distinct()
    
    
    context = {
        'area': Area.objects.all(),
        'genres': Genre.objects.all(),
        'genres_vn': genres_vn,
        'genres_hq': genres_hq,
        'genres_usuk': genres_usuk,
        'albums': album,
        'tracks': tracks,
        'vn': album_vn,
        'hq': album_hanquoc,
        'usuk': album_usuk,
        
    }
    return render(request, 'music/genre.html', context=context)

def genre_info(request, slug):
    genre = Genre.objects.filter(slug=slug)[0]
    tracks = Track.objects.filter(genres__slug = slug).order_by('-created_at')
    albums = Album.objects.filter(tracks__genres__slug = slug).distinct()
    print(tracks)
    context ={
        'genre': genre,
        'tracks': tracks,
        'albums': albums
    }
    return render(request, 'music/genre_info.html', context=context)


def artist_view(request):
    page = request.GET.get('page')
    limit = request.GET.get("limit")
    
    if not limit or not limit.isnumeric():
        limit = settings.LIMIT_DEFAULT
    
    keyword = request.GET.get('keywordInput')
    if keyword:
        artists = Artist.objects.filter(name__contains = keyword).values().order_by("-created_at")
    else:
        artists = Artist.objects.all().order_by("-created_at")
    
    artists_paginator = Paginator(artists,limit)
    try:
        artists_paginator = artists_paginator.page(page)
    except PageNotAnInteger:
        artists_paginator = artists_paginator.page(1)
    except EmptyPage:
        artists_paginator = artists_paginator.page(artists_paginator.num_pages)
    
    
    context = {
        'artists': artists_paginator,
        "keywordInput": keyword if keyword else "",
        "key": slugify(keyword) if keyword else ""
    }
    return render(request, 'music/artist.html', context=context)

def artist_info(request, slug):
    artist = Artist.objects.filter(slug=slug)[0]
    tracks = Track.objects.filter(artists__slug = slug)
        
    albums = Album.objects.filter(artists__slug = slug)
    userartist = None
    try:
        userartist = UserArtist.objects.get(user = request.user, artist = artist)
    except UserArtist.DoesNotExist:
        UserArtist.objects.create(user = request.user, artist=artist)
        userartist = UserArtist.objects.get(user = request.user, artist = artist)
        
    context = {
        'artist': artist,
        'tracks': tracks,
        'albums': albums,
        'userartist': userartist
    }
    return render(request, 'music/artist_info.html', context)

def album_view(request,slug):
    album= Album.objects.filter(slug=slug)
    tracks = Track.objects.filter(slug__in = album.values_list('tracks__slug',flat=True))
    artists = Artist.objects.filter(slug__in = album.values_list('artists__slug',flat=True))
    context={
        'album':album[0],
        'tracks':tracks,
        'artists': artists
    }
    return render(request, 'music/album.html', context)

def track_view(request, slug):
    track = Track.objects.filter(slug=slug)
    lyric = Lyric.objects.filter(name__in = track.values_list('lyrics__name'))
    track[0].increase_stream()
    context = {
        'track': track[0]
    }
    return render(request, 'music/track.html', context)

def artist_follow(request, slug):
    artist = Artist.objects.get(slug=slug)
    user = request.user
    userartist = UserArtist.objects.get(user=user,artist=artist)
    print(userartist.is_follow)
    userartist.follow()
    return redirect('music:artist_info',slug)
