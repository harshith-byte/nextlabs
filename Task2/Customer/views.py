
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.urls import reverse

from Customer.models import *
from api.forms import create_task_form
from api.models import Task
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
import requests
from django.contrib.auth.decorators import login_required
# Create your views here.

# Customer Home
@login_required(login_url='customer_login/')
def home(request):
    if request.user.is_customer and request.user.is_authenticated:
        user=request.user
        form=CustomerDetails.objects.filter(username=user)
        content={'form':form}

        return render(request, "Customer/home.html",content)
    else:
        return render(request,'Administrator/unauthorized.html')

# LOgout
def logout_view(request):       
    logout(request)
    return redirect('customer_login')


# Login
def  login_view(request):       
    if request.user.is_authenticated and request.user.is_customer:
        user=request.user
        form=CustomerDetails.objects.filter(username=user)
        content={'form':form}

        return render(request, "Customer/home.html",content)
    if request.method=='POST':
        username   = request.POST.get('username')
        password = request.POST.get('password')
        user =  authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            return redirect('customer_home')
        else:
            messages.error(request,"Username or password is incorrect")
    
        
    return render(request, "Customer/customerlogin.html")


# Customer Details
@login_required(login_url='customer_login/')
def customer_details(request):

    if request.user.is_authenticated and request.user.is_customer:

        username = request.user
        if request.method=="POST":
            form=CustomerDetails(username=username,
                            Firstname=request.POST.get('Firstname'),
                            Lastname=request.POST.get('Lastname'),
                            DOB=request.POST.get('DOB'),
                            phone=request.POST.get('phone'),
                            Address=request.POST.get('Address'))
            form.save()
            user=request.user
            form=CustomerDetails.objects.filter(username=user)
            
            content={'form':form}
            return render(request, 'Customer/home.html',content)
        return render(request,"Customer/customer_details.html")
    else:
        return render(request,'Administrator/unauthorized.html')    

# List Task
@login_required(login_url='customer_login/')
def listapps(request):
    if request.user.is_authenticated and request.user.is_customer:
        user=request.user
        form=CustomerDetails.objects.filter(username=user)
        task=Task.objects.get_queryset().order_by('id').filter(work="pending")
        page = request.GET.get('page', 1)

        paginator = Paginator(task, 4)

        users = paginator.page(page)

        content={'form':form,'list':task,'users': users }

        return render(request,'Customer/listapps.html',content)

    else:
        return render(request,'Administrator/unauthorized.html')    

# Update Profile
@login_required(login_url='customer_login/')
def updateprofile(request):
    if request.user.is_authenticated and request.user.is_customer:
        user=request.user
        obj=CustomerDetails.objects.filter(username=user)
        content={'form':obj}
        if request.user.is_authenticated:
            username = request.user
            if request.method=="POST":
                form=obj.update(
                            Firstname=request.POST.get('Firstname'),
                            Lastname=request.POST.get('Lastname'),
                            DOB=request.POST.get('DOB'),
                            phone=request.POST.get('phone'),
                            Address=request.POST.get('Address'))
            
                
                return render(request, 'Customer/home.html',content)
        return render(request,'Customer/updateprofile.html',content)
    else:
        return render(request,'Administrator/unauthorized.html')    
    
# API for uploading Screenshot
@api_view(['POST'])
def task_update_screenshot_api(request,pk):

    task=Task.objects.filter(id=pk)
    if request.method=="POST":
        serialize=task.update(Screenshot=request.data['Screenshot'],work=request.data['work'],completed_by=request.data['completed_by'])

        return Response(serialize,status.HTTP_201_CREATED)


# Method to add screenshot
@login_required(login_url='customer_login/')
def addscreenshot(request,pk):
    if request.user.is_authenticated and request.user.is_customer:
        user=request.user
        obj=CustomerDetails.objects.filter(username=user)
        src=create_task_form(request.POST,request.FILES)

        task=Task.objects.filter(id=pk)
        print(user.id)

        content={'form':obj,'task':task,'src':src}
        print(task)
        if request.method=="POST":

            data={
                'Screenshot':request.POST.get('screenshot'),
                'work':'completed',
                'completed_by':user.id
                }
            
            headers={'Content-Type': 'application/json'}
            print(data)
            r=requests.post('http://0.0.0.0:8000/customer/task_update_screenshot_api/'+pk+"/",json=data,headers=headers)
            tpoints=""
            for t in Task.objects.filter(id=pk):
                tpoints=t.points
            for ob in CustomerDetails.objects.filter(username=user):
                obpoints=ob.points
            obj.update(points=obpoints+tpoints)
            return HttpResponseRedirect(reverse('listtask'))

        
        return render(request,'Customer/addscreenshot.html',content)
    else:
        return render(request,'Administrator/unauthorized.html')    

# Method to list task completed by customer
def completedtask(request):
    if request.user.is_authenticated and request.user.is_customer:
        user=request.user
        obj=CustomerDetails.objects.filter(username=user)
    
        task=Task.objects.filter(completed_by=user.id)
        print(task)

        content={'form':obj,'task':task}
        return render(request,'Customer/completed_task.html',content)
    else:
        return render(request,'Administrator/unauthorized.html')    