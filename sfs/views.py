from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from shared_lib.sfs_core.models import *
from django.views import View
from django.contrib import messages
from django.urls import reverse
from shared_lib.utils.models import *

import firebase_admin

from firebase_admin import auth, credentials

from pathlib import Path
from django.conf import settings



# Create your views here.
class Home(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("access-restricted")


        print(request.user.is_authenticated)
        blue_cat = BpCat.objects.order_by('-id')[:5]
        print(request.resolver_match.url_name)
        views = BpDlv.objects.filter(type="view").count()

        blueprints = BP.objects.filter(status="approved").order_by('-id')[:5]
        return render(request, "sfs.html", {
            "blue_cats": blue_cat, 
            "blueprints": blueprints,
            "total_views": views,
            "total_downloads": BpDlv.objects.filter(type="download").count(),
            "total_likes": BpDlv.objects.filter(type="like").count(),
            "total_shares": BpDlv.objects.filter(type="share").count(),
            })
    
    def post(self, request):
        if not request.user.is_authenticated:

            return redirect("access_restricted")




def firebase_users(request):
    if not request.user.is_authenticated:
        return redirect("access-restricted")

    if not firebase_admin._apps:

        cred = credentials.Certificate(
            Path(settings.BASE_DIR) / "sfs.json"
        )

    firebase_admin.initialize_app(cred)
    users = []

    try:
        page = auth.list_users()

        while page:

            for user in page.users:

                users.append({
                    "uid": user.uid,
                    "email": user.email,
                    "phone_number": user.phone_number,
                    "display_name": user.display_name,
                    "photo_url": user.photo_url,
                    "disabled": user.disabled,
                    
                })

            page = page.get_next_page()

        return JsonResponse({
            "success": True,
            "count": len(users),
            "users": users
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "error": str(e)
        }, status=500)

def send(request):
    pass


def blueprint(request, bp_id):

    if not request.user.is_authenticated:
        return redirect("access-restricted")
    
    bp_id = request.GET.get('blueprint_id', '')
    
    if bp_id:
        bp = BP.objects.filter(bp_id=bp_id).first()
        if bp:

            return render(request, "blueprints.html", {"bp": bp})
        else:

            return HttpResponse("bp is wrong")
    else:

        return HttpResponse("bp id is missing")


def logs(request):

    if not request.user.is_authenticated:
        return redirect("access-restricted")
    logs = AllErrors.objects.order_by('-id')[:10]
    return render(request, "logs.html", {"logs": logs})

def users(request):

    if not request.user.is_authenticated:
        return redirect("access-restricted")
        
    return render(request, "sfs_users.html", {"users": AllUsers.objects.all()})


def categories(request):

    if not request.user.is_authenticated:
        return redirect("access-restricted")

    
    return render(request, "categories.html", {"categories": BpCat.objects.all()})

def blueprints(request):

    if not request.user.is_authenticated:
        return redirect("access-restricted")
    off = request.GET.get('off', '')
    if off:
        bp = BP.objects.filter(type="blueprint")[int(off)*10:(int(off)*10 + 10)]
    else:
        bp = BP.objects.filter(type="blueprint")[:10]
    return render(request, "blueprints.html", {"bps": bp})


def sfs_home(request):
    if not request.user.is_authenticated:
        return redirect("access-restricted")
    pass


class UploadCat(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("access-restricted")
        return render(request, "upload_category.html")
    
    def post(self, request):
        pass


class UploadBp(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("access-restricted")
        return render(request, "upload_bp.html")
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("access-restricted")
        name = request.POST.get('name', '')       
        type = request.POST.get('type', '')
        link = request.POST.get('link', '')
        zip_file = request.POST.get('zip_file', '')
        images = request.POST.getlist("images", [])

        if name and type and zip_file and images:

            if link:
                bp = BP.objects.create(
                    name = name,
                    type = type,
                    
                )

                messages.success(request, "Blueprint uploaded successfully.")
                return redirect(reverse("sfs:blueprints"))
            else:
                pass
        
        else:
            messages.error(request, "Please fill all the fields.")
            return redirect(reverse("sfs:upload_bp"))


class EditBp(View):
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("access-restricted")
        bp_id = request.GET.get('bp_id', '')

        if bp_id:
            bp = BP.objects.filter(bp_id=bp_id).first()
            if bp:
                return render(request, "edit_bp.html", {"bp": bp})
            else:
                messages.error("Blueprint not found.")
                return redirect("bp_edit.html")
        else: 
            return redirect("sfs:AccessRestriced")
    

    def put(request):
        return HttpResponse("put method called")
    
    def post(request):
        if not request.user.is_authenticated:
            return redirect("access-restricted")
        bp_id = request.POST.get('bp_id', '')
        name = request.POST.get('name', '')
        image = request.POST.get('image', '')

        if name and image:
            bp = BP.objects.filter(bp_id = bp_id).first()

            if bp:
                bp.name = name
                bp.save()
                return render(request, "edit_bp.html")
            
        return render(request, "edit_bp.html")


class EditCat(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("access-restricted")
        cat_id= request.GET.get('category_id', '')
        if cat_id:

            return render(request, "edit_cat.html")
        else:
            return redirect("sfs:AccessRestriced")
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("access-restricted")
        bp_id = request.POST.get('bp_id', '')
        name = request.POST.get('name', '')
        image = request.POST.get('image', '')

        if name and image:
            bp = BP.objects.filter(bp_id = bp_id).first()

            if bp:
                bp.name = name
                bp.save()
                return render(request, "edit_cat.html")

        else:
            messages.error(request, "Please fill all the fields.")
            return render(request, "edit_cat.html")

