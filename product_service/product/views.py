from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

def list_books(request):
    books = Book.objects.all()
    return render(request, 'book_management.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        price = request.POST.get('price')
        available = request.POST.get('available', False) == 'on'
        Book.objects.create(title=title, author=author, genre=genre, price=price, available=available)
        return redirect('list_books')
    return render(request, 'add_book.html')

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('list_books')

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'book_management.html', {'books': books, 'query': query})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    