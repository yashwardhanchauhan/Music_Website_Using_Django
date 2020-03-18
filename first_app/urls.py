from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('songs/<str:category>',views.songs,name='songs'),
    path('play/<str:song_name>',views.play,name='play'),
    path('register',views.register, name='register'),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout")
    
    
]