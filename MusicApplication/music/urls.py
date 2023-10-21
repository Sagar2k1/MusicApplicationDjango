from django.contrib import admin
from django.urls import path
from .views import artist_view, artist_info, genre_view, genre_info, album_view, search, track_view,artist_follow

app_name = 'music'
urlpatterns = [
    path('nghe-si/',artist_view, name = 'artist'),
    path('nghe-si/<slug:slug>',artist_info, name = 'artist_info'),
    path('nghe-si/<slug:slug>/follow',artist_follow, name = 'artist_follow'),
    path('the-loai/', genre_view,name='genre'),
    path('the-loai/<slug:slug>',genre_info,name='genre_info'),
    path('album/<slug:slug>',album_view,name='album'),
    path('tim-kiem/',search,name='search'),
    path('bai-hat/<slug:slug>',track_view,name='track'),
    
]