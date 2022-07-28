from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    #when you create a form you also use the user module and you need to nest 
    #a meta class in the user registration form 

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

#you need to build your own registration build 