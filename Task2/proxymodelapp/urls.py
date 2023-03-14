from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin_signup/',views.registration_view,name="admin_signup"),
    path('',views.registration_view_customer,name="customer_signup"),
]