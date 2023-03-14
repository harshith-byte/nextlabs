from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[

    # To list all open API'S
    path("task_api/", views.apioverview ,name="apioverview"),

    # List tasks which has status as pending
    path('task_list_api/',views.task_list_api,name="task_list_api"),

    # Create Task API
    path("task_create_api/", views.task_create_api, name="task_create_api"),
    
    # Update Task API using Task ID
    path("task_update_api/<str:pk>/", views.task_update_api, name="task_update_api"),
    
    # Delete Task API using Task ID
    path("task_delete_api/<str:pk>/", views.task_delete_api, name="task_delete_api")
]