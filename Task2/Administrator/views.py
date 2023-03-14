from django.shortcuts import redirect, render

from api.views import *

import json

from django.contrib.auth.decorators import login_required

from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Logout Method
def logout_view(request):       
    logout(request)
    return redirect('admin_login')

# Login Method
def  login_view(request):       #login function
    if request.user.is_authenticated and request.user.is_administrator:
        user=request.user
        form=Details.objects.filter(username=user)
        content={'form':form}

        return render(request, "Administrator/home.html",content)
    if request.method=='POST':
        username   = request.POST.get('username')
        password = request.POST.get('password')
        user =  authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            return redirect('admin_home')
        else:
            messages.error(request,"Username or password is incorrect")
    
        
    return render(request,'Administrator/adminlogin.html')


# Admin Details Method
@login_required(login_url='')
def admin_details(request):

    if request.user.is_administrator and request.user.is_authenticated:
        username = request.user
        if request.method=="POST":
            form=Details(username=username,
                         Firstname=request.POST.get('Firstname'),
                         Lastname=request.POST.get('Lastname'),
                         DOB=request.POST.get('DOB'),
                         phone=request.POST.get('phone'),
                         Address=request.POST.get('Address'))
            form.save()
            user=request.user
            form=Details.objects.filter(username=user)
            
            content={'form':form}
            return render(request, 'Administrator/home.html',content)
        return render(request,"Administrator/admin_details.html")
    else:
        return render(request,'Administrator/unauthorized.html')    

# Admin Home Method
@login_required(login_url='')
def home(request):
    if request.user.is_administrator and request.user.is_authenticated:
        user=request.user
        form=Details.objects.filter(username=user)
        content={'form':form}
    
        return render(request,"Administrator/home.html",content)
    else:
        return render(request,'Administrator/unauthorized.html')


# Admin List Task Method
@login_required(login_url='')
def listapps(request):
    if request.user.is_administrator and request.user.is_authenticated:
        user=request.user
        form=Details.objects.filter(username=user)
        task=Task.objects.get_queryset().order_by('id')
        page = request.GET.get('page', 1)

        paginator = Paginator(task, 4)

        users = paginator.page(page)

        content={'form':form,'list':task,'users': users }

        return render(request,'Administrator/listapps.html',content)
    else:
        return render(request,'Administrator/unauthorized.html')
    

# Admin Create Task Method 
@login_required(login_url='')
def Create_task(request):
    if request.user.is_administrator and request.user.is_authenticated:
        user=request.user
        form=Details.objects.filter(username=user)
        obj=Task.objects.get_queryset().order_by('id')
        page = request.GET.get('page', 1)

        paginator = Paginator(obj, 4)

        users = paginator.page(page)
        content={'form':form,'obj':obj,'users': users}
        if request.method=="POST":

            app_name=request.POST.get('appname')
            category_name=request.POST.get('categoryname')
            subcategory_name=request.POST.get('subcategoryname')
            app_subcategory=request.POST.get('appsubcategory')
            try:
                Task.objects.get(appname=app_name,categoryname=category_name,subcategoryname=subcategory_name,appsubcategory=app_subcategory)
                return render(request, 'Administrator/addapps.html',context={'message':"this Category has been created"})
            except ObjectDoesNotExist:
                data={"appname":app_name,
                    "categoryname":request.POST.get('categoryname'),
                    "subcategoryname":request.POST.get('subcategoryname'),
                    "appsubcategory":request.POST.get('appsubcategory'),
                    "points":request.POST.get('points')
                    }
                    
                print(data)
                headers={'Content-Type': 'application/json'}

                r=requests.post('http://0.0.0.0:8000/api/task_create_api/',json=data,headers=headers)

                return HttpResponseRedirect(reverse('admin_home'))
        else:
            return render(request, 'Administrator/addapps.html',content)
    else:
        return render(request,'Administrator/unauthorized.html')


# Admin update task Method
@login_required(login_url='')
def updateapps(request,pk):
    if request.user.is_administrator and request.user.is_authenticated:
        user=request.user
        form=Details.objects.filter(username=user)
        task=Task.objects.filter(id=pk)
        content={'form':form,'task':task}
        if request.method=="POST":

            app_name=request.POST.get('appname')

            category_name=request.POST.get('categoryname')
            subcategory_name=request.POST.get('subcategoryname')
            app_subcategory=request.POST.get('appsubcategory')

            try:
                Task.objects.get(appname=app_name,categoryname=category_name,subcategoryname=subcategory_name,appsubcategory=app_subcategory)
                return render(request, 'Administrator/addapps.html',context={'message':"this Category has been created"})
            except ObjectDoesNotExist:
                data={'appname':app_name,
                    'categoryname':request.POST.get('categoryname'),
                    'subcategoryname':request.POST.get('subcategoryname'),
                    'appsubcategory':request.POST.get('appsubcategory'),
                    'points':request.POST.get('points')
                    }
                print(data)
                headers={'Content-Type': 'application/json'}

                r=requests.post('http://0.0.0.0:8000/api/task_update_api/'+pk+"/",json=data,headers=headers)

                return HttpResponseRedirect(reverse('listapps'))
        else:
            return render(request, 'Administrator/updateapps.html',content)
    else:
        return render(request,'Administrator/unauthorized.html')

# Admin update profile Method
@login_required(login_url='')
def updateprofile(request):
    if request.user.is_administrator and request.user.is_authenticated:
        user=request.user
        form=Details.objects.filter(username=user)
        content={'form':form}

        if request.method=="POST":
            form=form.update(
                        Firstname=request.POST.get('Firstname'),
                        Lastname=request.POST.get('Lastname'),
                        DOB=request.POST.get('DOB'),
                        phone=request.POST.get('phone'),
                        Address=request.POST.get('Address'))
        
            
            return render(request, 'Administrator/home.html',content)
        return render(request,'Administrator/updateprofile.html',content)
    else:
        return render(request,'Administrator/unauthorized.html')


# Admin Delete task Method
@login_required(login_url='')
def deleteapp(request,pk):
    if request.user.is_administrator and request.user.is_authenticated:
        user=request.user
        form=Details.objects.filter(username=user)
        task=Task.objects.get_queryset().order_by('id')
        page = request.GET.get('page', 1)
        paginator = Paginator(task, 4)
        users = paginator.page(page)
        content={'form':form,'list':task,'users':users}
        task=Task.objects.get(id=pk)
        task.delete()

        return render(request, 'Administrator/listapps.html',content) 
    else:
        return render(request,'Administrator/unauthorized.html')
