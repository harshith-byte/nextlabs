from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

from proxymodelapp.models import Administrator
# manager for custom model 

class Details(models.Model):

    username=models.OneToOneField(Administrator, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=20)
    Lastname=models.CharField(max_length=20)
    DOB=models.DateField()
    phone=models.BigIntegerField(blank=True)
    Address=models.TextField(max_length=50)
    def __str__(self):
        return self.Firstname
