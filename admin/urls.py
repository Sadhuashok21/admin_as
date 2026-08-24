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
from django.conf import settings
from django.conf.urls.static import static

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
    path('access-restricted', views.access_restricted, name="access-restricted")
] 

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)




handler404 = 'admin.views.er_404'
handler400 = 'admin.views.er_400'
handler401 = 'admin.views.er_401'
handler403 = 'admin.views.er_403'
handler408 = 'admin.views.er_408'
handler500 = 'admin.views.er_500'
handler502 = 'admin.views.er_502'
handler503 = 'admin.views.er_503'
handler504 = 'admin.views.er_504'
handler505 = 'admin.views.er_505'

