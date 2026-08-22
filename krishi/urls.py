from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="krishi_index"),
    path("access_restricted", access_restricted, name="access_restricted")
]
