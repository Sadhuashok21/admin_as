from django.shortcuts import render

def admin(request):
    return render(request, "home.html")

def home(request):
    return render(request, "home.html")