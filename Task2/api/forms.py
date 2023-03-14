from django import forms
from .models import *

class create_task_form(forms.ModelForm):
    
    class Meta:
      model = Task
      fields= '__all__'