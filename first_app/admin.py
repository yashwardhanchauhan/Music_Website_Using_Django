from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from .models import Song,song_to_playlist,Album,playlist


admin.site.register(Song)
admin.site.register(playlist)
admin.site.register(Album)
admin.site.register(song_to_playlist)