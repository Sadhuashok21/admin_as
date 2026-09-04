from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="sfs_index"),
    path('blueprints', views.blueprints, name="blueprints"),
    path('planets', views.pla_wor, name="planets"),
    path('blueprints/blueprint/<str:bp_id>', views.blueprint, name="blueprint"),
    path('sfs_home', views.sfs_home, name="sfs_home"),
    path('upload_category', views.UploadCat.as_view(), name="upload_category"),
    path('upload_bp', views.UploadBp.as_view(), name="upload_bp"),
    path('edit_category', views.EditCat.as_view(), name="edit_cat"),
    path('edit_bp', views.EditBp.as_view(), name="edit_bp"),
    path('logs', views.logs, name="logs"),
    path('users', views.users, name="users"),
    path('categories', views.categories, name="categories"),

    path('sfs-users/', views.firebase_users, name="users"),

    
]
