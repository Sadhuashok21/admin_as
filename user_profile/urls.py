from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="profile_index"),
    path('log_activity', views.log_activity, name="log_activity")
]
