from django import forms 
from .models import Book

class NewBookForm(forms.ModelForm): 
    class Meta:
        model = Book
        fields = ['title']

class BorrowBookForm(forms.ModelForm):

    class Meta:
        model = Book 
        fields = ['author']
        widgets = {'author': forms.HiddenInput}

#HERE WE ARE CREATING OUR FORM CLASSES AND THE FIELDS THAT THEY WILL CONTAIN 