
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class AdminDetailForm(forms.ModelForm):
    
    class Meta:
        model = Details
        fields = '__all__'
