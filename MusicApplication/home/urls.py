from django.contrib import admin
from django.urls import path
from .views import home, search, login_view, logout_view

app_name = 'home'
urlpatterns = [
    path('', home, name = 'home'),
    path('search/<slug:keyword>/', search,name = 'search'),
    path("login/",login_view, name="login_view"),
    path('logout/', logout_view, name = 'logout')
    
]