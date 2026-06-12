from django.shortcuts import render
#from 

# Create your views here.
def index(request):
    return render(request, "sonicora.html")


def movie_upload(request):
    return render(request, "movie_upload.html")


def song_upload(request):
    return render(request, "song_upload.html")

def hero_upload(request):
    return render(request, "hero.html")