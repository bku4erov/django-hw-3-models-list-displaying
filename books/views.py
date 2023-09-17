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

def books_by_date(request, pub_date):
    template = 'books/books_catalog.html'
    books = Book.objects.filter(pub_date=pub_date)
    context = {'books': books}
    prev_book_by_date = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    if prev_book_by_date:
        context['prev_date'] = prev_book_by_date.pub_date
        context['prev_date_str'] = prev_book_by_date.pub_date.strftime('%Y-%m-%d')
    next_book_by_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    if next_book_by_date:
        context['next_date'] = next_book_by_date.pub_date
        context['next_date_str'] = next_book_by_date.pub_date.strftime('%Y-%m-%d')
    
    return render(request, template, context)