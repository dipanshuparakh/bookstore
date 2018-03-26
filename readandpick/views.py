from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render

from .models import Book


def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'readandpick/book_list.html', context)


def book_details(request, id):
    book = Book.objects.get(id=id)  
    context = {'book': book}
    return render(request, 'readandpick/book_details.html', context)
