
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# List all Open API'S
@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'task_list_api':'/api/task_list_api/',                 #Read
        'task_create_api':'/api/task_create_api/',             #Create Task
        'task_update_api':'/api/task_update_api/<str:pk>/',    #Update Task
        'task_delete_api':'/api/task_delete_api/<str:pk>/'     #delete Task 
    }
    return Response(api_urls)


# List Task with status as "Pending"
@api_view(['GET'])
def task_list_api(request):
    if request.user.is_authenticated:
        task=Task.objects.filter(work="pending")
        serializers=TaskSerializer(task, many=True)

        return Response(serializers.data)
    else:
        return render(request,'Administrator/unauthorized.html')

# Create Task API
@api_view(['POST'])
def task_create_api(request):

    if request.method=="POST":
        serialize=TaskSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status.HTTP_201_CREATED)
        print(serialize.errors)
        return Response(serialize.data,status.HTTP_400_BAD_REQUEST)



# Update Task API using Task ID
@api_view(['POST'])
def task_update_api(request,pk):
    task=Task.objects.filter(id=pk)
    if request.method=="POST":
        serialize=task.update(appname=request.data['appname'],
                                    categoryname=request.data['categoryname'],
                                    subcategoryname=request.data['subcategoryname'],
                                    appsubcategory=request.data['appsubcategory'],
                                    points=request.data['points'])

        return Response(serialize,status.HTTP_201_CREATED)

# Delete Task using Task ID
def task_delete_api(request,pk):

    task=Task.objects.get(id=pk)
    task.delete()
    return HttpResponseRedirect(reverse())


