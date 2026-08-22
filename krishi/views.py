from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not  request.user.is_authenticated:
        return redirect("access")
    
    return render(request, "krishi.html")

def access_restricted(request):

    return render(request, "access_restricted.html")