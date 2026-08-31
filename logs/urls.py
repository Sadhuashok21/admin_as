from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="logs_index"),
    path('errors/', errors, name="errors"),
    path('total_activity/', total_activity, name="total_activity"),
]