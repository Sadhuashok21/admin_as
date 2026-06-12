from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from shared_lib.sfs_core.models import *
from django.views import View
from django.contrib import messages
from django.urls import reverse
from shared_lib.utils.models import *

# Create your views here.

class Home(View):
    def get(self, request):
        blue_cat = BpCat.objects.all()

        views = BpDlv.objects.filter(type="view").count()
        
        blueprints = BP.objects.filter(status="approved").order_by('-id')[:10]
        return render(request, "sfs.html", {
            "blue_cats": blue_cat, 
            "blueprints": blueprints,
            "total_views": views,
            "total_downloads": BpDlv.objects.filter(type="download").count(),
            "total_likes": BpDlv.objects.filter(type="like").count(),
            "total_shares": BpDlv.objects.filter(type="share").count(),
            })
    
    def post(self, request):
        return redirect("sfs:AccessRestriced")



def blueprints(request):
    bp_id = request.GET.get('blueprint_id', '')

    if bp_id:
        bp = BP.objects.filter(blueprint_id=bp_id).first()
        if bp:

            return render(request, "blueprints.html", {"bp": bp})
        else:

            return HttpResponse("bp is wrong")
    else:

        return HttpResponse("bp id is missing")

def sfs_home(request):
    pass


class UploadCat(View):
    def get(self, request):
        return render(request, "upload_category.html")
    
    def post(self, request):
        pass


class UploadBp(View):
    def get(self, request):
        return render(request, "upload_bp.html")
    
    def post(self, request):
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
        bp_id = request.GET.get('bp_id', '')

        if bp_id:
            bp = BP.objects.filter(blueprint_id=bp_id).first()
            if bp:
                return render(request, "edit_bp.html", {"bp": bp})
            else:
                messages.error("Blueprint not found.")
                return redirect("bp_edit.html")
        else: 
            return redirect("sfs:AccessRestriced")
    
    
    def post(request):
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


class AccessRestriced(View):
    def get(self, request):
        return render(request, "access_restricted.html")

class EditCat(View):
    def get(self, request):
        cat_id= request.GET.get('category_id', '')
        if cat_id:

            return render(request, "edit_cat.html")
        else:
            return redirect("sfs:AccessRestriced")
    
    def post(self, request):
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

