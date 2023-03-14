from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):

    class Meta:
        model = Administrator
        fields = ('email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['username'],self.fields['password1'],self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control '})

class RegistrationFormCustomer(UserCreationForm):

    class Meta:
        model = Customer
        fields = ('email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(RegistrationFormCustomer, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['username'],self.fields['password1'],self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control '})