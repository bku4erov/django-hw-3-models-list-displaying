from django.shortcuts import redirect, render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

def books_catalog(request):
    template = 'books/books_catalog.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def books_by_date(request, date):
    pass