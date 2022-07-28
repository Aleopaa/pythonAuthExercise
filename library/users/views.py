from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
from django.contrib import messages
# Create your models here.

def register(req):
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            ##that function checks if all the fields are valid if so it will create data filled with all user data 
            form.save()
            username = form.cleaned_data.get('username') ##cleaned data dict is created 
            ##the only reason we are passing the username is because of the sucess message
            messages.success(req, f'Welcome, {username}')
            ##you want to be redirected somewhere after you fill in the form
            return redirect('catalogue-home')#we can pass the name attribute of the page here 
    else:
            form = UserRegistrationForm()
    data = {'form': form}
    return render(req, 'register.html', data)