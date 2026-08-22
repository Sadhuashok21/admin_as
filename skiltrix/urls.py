from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="skiltrix_index"),
    path('internships/', Internships.as_view(), name="internships"),
    path('submissions/', submissions, name="submissions"),
    path('languages/add-language', AddLanguage.as_view(), name="add-language"),
    path('restriciton', restriciton, name="restriciton"),

    path('languages/', Language_.as_view(), name="languages"),

    path('companies/', Company.as_view(), name="companies"),
    path('courses/', Course.as_view(), name="courses"),
    path('videos/', Video.as_view(), name="videos"),

    path('code/', code, name="code"),
    path('users/', users, name="users"),
    path('files', FileSystem.as_view(), name="file-system"),
]
