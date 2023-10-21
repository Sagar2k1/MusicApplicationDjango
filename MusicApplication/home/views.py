from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from music import models
from music.models import Track, Album, Artist, Genre
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

# Create your views here.
def base(request):
    models.set_trend_track()
    keyword = request.GET.get('keywordInput')
    # đăng nhập
    context = {
        'keywordInput': keyword if keyword else ""
    } 
    return render(request, 'home/base.html', context=context)

def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password= password)
        if user:
            login(request, user)
            return redirect('home:home')
        else:
            error='Invalid username or password.'
    context = {
        "error": error
    }
    return render(request, 'home/login.html',context=context)
    
def logout_view(request):
    logout(request)
    return redirect('home:home')

def home(request):
    tracks = Track.objects.all().order_by('-streams')
    albums = Album.objects.all()
    
    # top 10
    if Track.objects.all().__len__()<10:
        tracks = Track.objects.all().order_by('-streams')
    else:
        tracks = Track.objects.all().order_by('-streams')[:10]
    
    tracks2 = None
    if Track.objects.all().__len__()<100:
        tracks2 = Track.objects.all().order_by('-streams')      
    else:
        tracks2 = Track.objects.all().order_by('-streams')[:100]
    
    
    context = {
        'genres': Genre.objects.all(),
        'tracks': tracks,
        'tracks2': tracks2,
        'albums': albums,
        
    }
    return render(request, 'home/index.html', context=context)
'''
def search(request, keyword):
    keywordInput = request.GET.get(keyword) 
    tracks = Track.objects.filter(Q(name__contains=keywordInput)|Q(artists__name__contains=keywordInput)).values().order_by('-created_at')
    albums = Album.objects.filter(Q(name__contains=keywordInput)).values().order_by('-created_at')
    artists = Artist.objects.filter(Q(name__contains=keywordInput)).values().order_by('-created_at')
    context = {
        'tracks': tracks,
        'albums': albums,
        'artists': artists,
    }
    return (request, 'home/search.html', context)
'''

def top_100_view(request):
    
    return redirect('home:home')
    
    