from django.shortcuts import render, get_object_or_404

from authors_app.models import Author
from books_app.models import Book


def authors(request):
    authors_objects = Author.objects
    return render(request,'authors.html',{'authors':authors_objects})


def author_detail(request,author_id):
    author_details = get_object_or_404(Author, pk=author_id)
    books_filter = Book.objects.values('title', 'quantity', 'id').filter(authors=author_details.id)
    return render(request, 'authors_app/author_detail.html', {'books': books_filter, 'author': author_details})



