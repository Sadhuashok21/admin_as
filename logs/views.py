from django.shortcuts import render, redirect
from shared_lib.utils.models import *

# Create your views here.
def index(request):

    if request.user.is_authenticated:

        off = request.GET.get("off", 0)

        if off:
            logs = TotalActivity.objects.all().order_by('-id')[int(off) * 30:int(off) * 30 + 30]
        else:
            logs = TotalActivity.objects.all().order_by('-id')[:30]
        return render(request, "index_logs.html", {"logs": logs}    )
    else:
        return redirect('access-restricted')



def errors(request):
    if request.user.is_authenticated:

        off = request.GET.get("off", 0)

        if off:
            logs = AllErrors.objects.all().order_by('-id')[int(off) * 30:int(off) * 30 + 30]
        else:
            logs = AllErrors.objects.all().order_by('-id')[:30]
        return render(request, "index_logs.html", {"logs": logs}    )
    else:
        return redirect('access-restricted')


def total_activity(request):
    if request.user.is_authenticated:

        off = request.GET.get("off", 0)

        if off:
            logs = TotalActivity.objects.all().order_by('-id')[int(off) * 30:int(off) * 30 + 30]
        else:
            logs = TotalActivity.objects.all().order_by('-id')[:30]
        return render(request, "index_logs.html", {"logs": logs}    )
    else:
        return redirect('access-restricted')