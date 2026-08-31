from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from shared_lib.skiltrix_core.models import *
from shared_lib.utils.random import * 
from django.contrib import messages
import json, os
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt

load_dotenv()

# Create your views here.

class FileSystem(View):
    def get(self, request):
        return render(request, "cke-editor.html")

    def post(self, request):
        pass


def index(request):
    if request.user.is_authenticated:
        return render(request, "st_index.html")
    else:
        
        return redirect("skiltrix:restriciton")

def users(request):
    
    if request.user.is_authenticated:
        return render(request, "st_users.html")
    else:
        return redirect("skiltrix:restriciton")


class Language_(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')

        languages = Language.objects.all()

        return render(request, "languages.html", {"languages": languages})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')


        data = json.loads(request.body)
        name = data.get('language', '')
        data_json = {
            "status": True,
            "message": "success",
        }
        if name:
            Language.objects.create(name=name, language_id = unique_id(), user_id = request.user.user_id)
        else:
            data_json.update({"message": "error"})
        
        return JsonResponse(data_json, safe=False)

    def delete(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')


        print("delete")
        data = json.loads(request.body)
        language_id = data.get('language_id', '')

        data_json = {
            "status": True,
            "message": "success",
        }

        if language_id:
            Language.objects.filter(language_id=language_id).delete()
        else:
            data_json.update({"message": "error"})

        return JsonResponse(data_json, safe=False)

        

def code(request):
    
    if not request.user.is_authenticated:
        return redirect('skiltrix:restriciton')

    return render(request, "code.html")

def restriciton(request):
    return render(request, "access_restricted.html")


    
class Internships(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "internships.html", {"internships": Internship.objects.all(), "company": Companies.objects.all()})
        else:
            return redirect("skiltrix:restriciton")

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')

        data = json.loads(request.body)

        data_json = {
            "status": True,
            "message": "success",
        }

        name = data.get('name', '')
        company = data.get('company', '')
        type = data.get('type', '')
        location = data.get('location', '')
        date = data.get('date', '')
        apply_link = data.get('apply_link', '')
        price = data.get('price', '')
        paid = data.get('paid', '')


        if name and company:
            Internship.objects.create(
                name = name,
                internship_id = unique_id(),
                company_id=company,
                apply_link=apply_link,
                type = type,
                is_paid = paid,
                deadline = date,
                location=location,
                price = price,
                )
        else:
            data_json.update({"message": "error"})

        return JsonResponse(data_json, safe=False)

    def delete(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')

        data = json.loads(request.body)

        data_json = {
            "status": True,
            "message": "success",
        }

        internship_id = data.get("internship_id", "")

        if internship_id:
            Internship.objects.filter(internship_id=internship_id).delete()
        else:
            data_json.update({"message": "error"})

        return JsonResponse(data_json, safe=False)

class AddLanguage(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')
        return render(request, "add-language.html")

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')

        name = request.POST.get('name', '')

        Language.objects.create(name = name, language_id = unique_id(), user_id = request.user.user_id)
        return render(request, "add-language.html")
       

class Course(View):

    def get(self, request):
        if request.user.is_authenticated:

            return render(request, "courses.html", {"courses": Courses.objects.all()})
        else:
            return redirect("skiltrix:restriciton")

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')

        data_json = {
            "status": True,
            "message": "success",
        }

        name = request.POST.get('name', '')
        image = request.FILES.get('image', '')
        is_paid = request.POST.get('paid', '')
        type = request.POST.get('type', '')
        price = request.POST.get('price', '')

        if name and image and is_paid and type and price:

            import boto3
            
            s3 = boto3.client(
                service_name="s3",
                endpoint_url=os.getenv("endpoint_url"),
                aws_access_key_id=os.getenv("aws_access_key_id"),
                aws_secret_access_key=os.getenv("aws_secret_access_key"),
                region_name="auto",
            )
            new_image = unique_id() + "." + image.name.split('.')[-1]
            
            response1 = s3.put_object(
                Bucket="sfs-blueprints",
                Key="st/images/" + new_image,
                Body=image,
                ContentType=image.content_type,
            )

            Courses.objects.create(
                name = name,
                course_id = unique_id(),
                user_id = request.user.user_id,
                type=type,
                is_paid=is_paid,
                image = new_image)
        else:
            data_json.update({"message": "error"})

        return JsonResponse(data_json, safe=False)

    def delete(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')

        data = json.loads(request.body)

        data_json = {
            "status": True,
            "message": "success",
        }

        course_id = data.get("course_id", "")

        if course_id:
            Courses.objects.filter(course_id=course_id).delete()
        else:
            data_json.update({"message": "error"})

        return JsonResponse(data_json, safe=False)


def submissions(request):
    if not request.user.is_authenticated:
        return redirect('skiltrix:restriciton')

    return render(request, "submissions.html")


class Video(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "videos.html", {"videos": Videos.objects.all(), "courses": Courses.objects.all()})
           
        else:
            return redirect("skiltrix:restriciton")

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')

        data_json = {
            "status": True,
            "message": "success",
        }

        title = request.POST.get('title', '')
        video = request.FILES.get('video', '')
        description = request.POST.get('description', '')
        course_id = request.POST.get('course', '')
        image = request.FILES.get('image', '')
            

        if title and video and description and course_id and image:

            import boto3
            
            s3 = boto3.client(
                service_name="s3",
                endpoint_url=os.getenv("endpoint_url"),
                aws_access_key_id=os.getenv("aws_access_key_id"),
                aws_secret_access_key=os.getenv("aws_secret_access_key"),
                region_name="auto",
            )
            new_image = unique_id() + "." + image.name.split('.')[-1]
            new_video = unique_id() + "." + video.name.split('.')[-1]
            
            response1 = s3.put_object(
                Bucket="sfs-blueprints",
                Key="st/videos/" + new_video,
                Body=video,
                ContentType=video.content_type,
            )

            response2 = s3.put_object(
                Bucket="sfs-blueprints",
                Key="st/images/" + new_image,
                Body=image,
                ContentType=image.content_type,
            )

            Videos.objects.create(
                title = title,
                video_id = unique_id(),
                user_id = request.user.user_id,
                course_id = course_id,
                description=description,
                video = new_video,
                image = new_image)
        else:
            data_json.update({"message": "error"})

        return JsonResponse(data_json, safe=False)

    def delete(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')

        data = json.loads(request.body)

        data_json = {
            "status": True,
            "message": "success",
        }

        video_id = data.get("video_id", "")

        if video_id:
            Videos.objects.filter(video_id=video_id).delete()
        else:
            data_json.update({"message": "error"})

        return JsonResponse(data_json, safe=False)



class Company(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')

        
        return render(request, 'companies.html', {"companies": Companies.objects.all()})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')
        
        name = request.POST.get('name', '')
        image = request.FILES.get('image', '')
        description = request.POST.get('description', '')


        data = {
            "status": True,
            "message": "success",
        }

        if name and image:
            import boto3

            s3 = boto3.client(
                service_name="s3",
                endpoint_url=os.getenv("endpoint_url"),
                aws_access_key_id=os.getenv("aws_access_key_id"),
                aws_secret_access_key=os.getenv("aws_secret_access_key"),
                region_name="auto",
            )

            new_image = unique_id() + "." + image.name.split('.')[-1]

            response1 = s3.put_object(
                Bucket="sfs-blueprints",
                Key="st/images/" + new_image,
                Body=image,
                ContentType=image.content_type,
            )
            Companies.objects.create(name=name, image=new_image, company_id = unique_id(), description=description)
            
        else:
            messages.error("error")
        return JsonResponse(data, safe=False)

    def delete(self, request):
        if not request.user.is_authenticated:
            return redirect('skiltrix:restriciton')

        data = json.loads(request.body)
        company_id = data.get('company_id', '')

        data_json = {
            "status": True,
            "message": "success",
        }
        if company_id:
            Companies.objects.filter(company_id=company_id).delete()
        else:
            data_json.update({"message": "error"})

        return JsonResponse(data_json, safe=False)



