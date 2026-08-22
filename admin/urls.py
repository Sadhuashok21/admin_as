"""
URL configuration for admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('krishi/', include(("krishi.urls", "krishi"), namespace="krishi")),
    path('sfs/', include(("sfs.urls", "sfs"), namespace="sfs"),),
    path('skiltrix/', include(("skiltrix.urls", "skiltrix"), namespace="skiltrix")),
    path('database/', include(("database.urls", "database"), namespace="database")),
    path('sonicora/', include(("sonicora.urls", "sonicora"), namespace="sonicora")),
    path('transport_hub/', include(('transport_hub.urls', "transport_hub"), namespace="transport_hub")),
    path('profile/', include(('user_profile.urls', 'profile'), namespace="profile")),
    path('', views.home, name="home"),
    path('logs/', include(("logs.urls", 'logs'), namespace="logs")),
] 
