from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required ##this decorator can be used anywhere if you want the user to have to login before accessing this page through the route and in general 
def books(request):
    data = {'bookos': Book.objects.all()}
    return render(request, 'book.html', data)


def show(request, id):
    book = get_object_or_404(Book, pk=id)
    # prints
    data = {'book': book}
    return render(request, 'show.html', data)

