from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

from proxymodelapp.models import Customer


class CustomerDetails(models.Model):

    username=models.OneToOneField(Customer, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=20)
    Lastname=models.CharField(max_length=20)
    DOB=models.DateField()
    phone=models.BigIntegerField(blank=True)
    Address=models.TextField(max_length=50)
    points=models.IntegerField(blank=True, default=0)
    def __str__(self):
        return self.Firstname
