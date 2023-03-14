from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    # Admin Home
    path('home/', views.home,name="admin_home"),

    # Admin Details 
    path('admin_details/',views.admin_details,name="admin_details"),

    # Admin Login 
    path('',views.login_view,name="admin_login"),

    # Admin Logout
    path('admin_logout/',views.logout_view,name="admin_logout"),

    # Admin List Task
    path('listapps/',views.listapps,name="listapps"),

    # Admin Create task
    path('Create_task/',views.Create_task,name="Create_task"),

    # Admin update task
    path('updateapps/<str:pk>/',views.updateapps,name="updateapps"),

    # Admin update profile
    path('updateprofile/',views.updateprofile,name="updateprofile"),

    # Admin delete task
    path('deleteapp/<str:pk>/',views.deleteapp,name="deleteapp"),

]