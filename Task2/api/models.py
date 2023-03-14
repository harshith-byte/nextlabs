
from django.db import models

from proxymodelapp.models import Customer

# Create your models here.
class Task(models.Model):
    Books='Books'
    Business='Business'
    Developer='Developer'
    Education='Education'
    Entertainment='Entertainment'
    AppCategory=(
        (Books,'Books'),
        (Business,'Business'),
        (Education,'Education'),
        (Entertainment,'Entertainment')
    )

    EReader='EReader'
    Fiction='Fiction'
    NonFiction='NonFiction'
    Accounting='Accounting'
    CRM='CRM'
    Database='Database'
    Desgin='Desgin'
    Development='Development'
    Language='Language'
    SocialMedia='SocialMedia'

    subcategory=(
        (EReader,'EReader'),
        (Fiction,'Fiction'),
        (NonFiction,'NonFiction'),
        (Accounting,'Accounting'),
        (CRM,'CRM'),
        (Database,'Database'),
        (Desgin,'Desgin'),
        (Development,'Development'),
        (Language,'Language'),
        (SocialMedia,'SocialMedia')
    )

    appname=models.CharField(max_length=50)
    categoryname=models.CharField(
        choices=AppCategory,
        default=Books,
        max_length=20
    )

    subcategoryname=models.CharField(max_length=50)
    appsubcategory=models.CharField(
        choices=subcategory,
        default=EReader,
        max_length=20
    )

    points=models.IntegerField()
    Screenshot=models.ImageField(upload_to='images/',blank=True)

    pending="pending"
    completed="completed"
    task=[
        (pending,"pending"),
        (completed,"completed")]
    work=models.CharField(choices=task, default=pending,max_length=10)

    completed_by=models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.appname

