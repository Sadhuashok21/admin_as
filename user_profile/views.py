from django.shortcuts import render

# Create your views here.
def index(request):
    if True:
        pass
    return render(request, "user_profile.html")


def log_activity(request):
    return render(request, "log_activity.html")