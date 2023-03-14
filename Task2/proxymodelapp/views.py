from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import redirect, render

from api.views import *

import json


from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
def homePage(request) : 
    return render(request ,  "proxymodelapp/homePage.html" )


def registration_view(request):      # signup function

    form = RegistrationForm()
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password1')
            user =  authenticate(request,username=user, password=password)
            if user:
                login(request, user)
                return redirect('admin_details')
        else:
            messages.error(request, "Please Correct Below Errors")
            context = {'form':form}
    else:
        
        context = {'form':form}
    return render(request, "Administrator/adminsignup.html", context)

def registration_view_customer(request):      # signup function

    form = RegistrationFormCustomer()
    context = {}
    if request.POST:
        form = RegistrationFormCustomer(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password1')
            user =  authenticate(request,username=user, password=password)
            if user:
                login(request, user)
                return redirect('customer_details')
        else:
            messages.error(request, "Please Correct Below Errors")
            context = {'form':form}
    else:
        
        context = {'form':form}
    return render(request, "Customer/customersignup.html", context)