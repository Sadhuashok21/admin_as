from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="sonicora_index"),
    path('/movie_upload', views.movie_upload, name="movie_upload"),
    path('/song_upload', views.song_upload, name="song_upload"),
    path('/hero_upload', views.hero_upload, name="hero_upload"),
    
]
