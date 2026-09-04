from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse

from shared_lib.sfs_core.models import AllUsers

# Create your views here.
class Home(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("access-restricted")

        off = request.GET.get("off", 0)

        if int(off) < 0 :
            off = 0
        if off:
            users = AllUsers.objects.order_by("-id")[int(off)*10:(int(off)*10 + 10)]
        else:
            users = AllUsers.objects.order_by("-id")[:10]
        return render(request, "u_index.html", {"users": users})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("access-restricted")

        user_id = request.POST.get('user_id', '')
        if user_id:
            AllUsers.objects.first(user_id=user_id).delete()

        url = f"users:users_index"
        return redirect(reverse(url))
        