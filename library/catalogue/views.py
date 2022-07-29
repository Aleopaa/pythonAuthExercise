from wsgiref.util import request_uri
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import BorrowBookForm, NewBookForm
from .models import Book


def home(request):
    return render(request, 'home.html')

    #HERE WE ARE RENDERING HOME.HTML

def about(request):
    return render(request, 'about.html')

    
    #HERE WE ARE RENDERING ABOUT.HTML

@login_required ##this decorator can be used anywhere if you want the user to have to login before accessing this page through the route and in general 
def books(request):
    data = {'bookos': Book.objects.all()}
    return render(request, 'book.html', data)

    #HERE WE ARE RENDERING BOOK.HTML WITH THE DATA OF ALL OF OUR BOOKS AFTER LOGIN 

@login_required
def show(request, id):
    book = get_object_or_404(Book, pk=id)
    # prints
    if request.method == "POST":
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            book.author = request.user 
            book.save()
            return redirect("catalogue-show", id=id)
    else:
        form = BorrowBookForm(initial={'author': request.user})
    data = {'book': book, 'form': form}
    return render(request, 'show.html', data)

    #HERE WE ARE GETTING OUR BOOK AND A PRIMARY KEY OF ID 
    #WE ARE LINKING THE USER TO THE AUTHOR AND SAVING IT
    #WE ARE THEN REDIRECTING THEM TO THE PAGE WHERE IT WILL DISPLAY THIS 
    #OTHERWISE IF THE USER IS LOGGED IN AND THEREFORE ALREADY THE AUTHOR IT WILL JUST SHOW THEM STRAIGHT AWAY 

@login_required
def create(request):
    if request.method == "POST":
        form = NewBookForm(request.POST)
        if form.is_valid():
            id = form.save().id #when a new dog is created we automatically get an id signed and then we get the id from that 
            return redirect('catalogue-show', id=id)#need to pass an id to show a specific dog 

    else:
        form = NewBookForm()
        data = {'form': form}
        return render(request, 'new.html', data)


        #WHAT IS HAPPENING IN THIS FILE?

        #HERE WE ARE TAKING HTTP RESPONSES AND RETURNING THEM
        #THIS IS WHERE WE SET UP THE FUNCTIONS THAT WILL BE TRIGGERED WHEN A PARTICULAR ROUTE IS ACCESSED 
        #THEY ARE PART OF THE USER INTERFACE THEY RENDER THE HTML IN YOUR TEMPLATE FILES INTO WHAT YOU SEE IN YOUR BROWSER WHEN YOU RENDER A WEB PAGE 
        #HERE WE ARE ALSO ADDING DECORATORS TO REQUIRE LOG IN BEFORE ACCESS 
        #HERE WE CREATE OUR POST, GET, DELETE REQS ETC 
