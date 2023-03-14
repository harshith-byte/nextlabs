from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    # Customer Home 
    path('home/', views.home,name="customer_home"),

    # Customer Detail
    path('customer_details/',views.customer_details,name="customer_details"),

    # Customer Login
    path('customer_login/',views.login_view,name="customer_login"),

    # Customer Logout
    path('customer_logout/',views.logout_view,name="customer_logout"),

    # List Pending Task
    path('listtask/',views.listapps,name="listtask"),

    # Update Customer Profile
    path('updatecustomerprofile/',views.updateprofile,name="updatecustomerprofile"),

    # Customer Must Add Screenshot
    path('addscreenshot/<str:pk>/',views.addscreenshot,name="addscreenshot"),

    # API For uploading Sceenshot using Task ID
    path('task_update_screenshot_api/<str:pk>/',views.task_update_screenshot_api,name="task_update_screenshot_api"),

    path('completedtask/',views.completedtask,name="completedtask")
]
