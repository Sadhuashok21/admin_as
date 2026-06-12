from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="skiltrix_index")    
]
