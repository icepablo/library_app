from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from orders_app.models import Order
from .models import Book


def home(request):
    return render(request, 'home.html')


def books(request):
    book_objects = Book.objects
    return render(request, 'books.html', {'books': book_objects})


def book_detail(request, book_id):
    book_object = get_object_or_404(Book, pk=book_id)
    return render(request, 'books_app/book_detail.html', {'book': book_object})


@login_required(login_url="/accounts/login")
def borrow(request, book_id):
    if request.method == 'POST':
        book_object = get_object_or_404(Book, pk=book_id)
        user_object = User.objects.get(id=request.user.id)
        order_object = Order()
        borrowed_books_filter = Order.objects.values('item').filter(customer__exact=user_object)
        borrowed_books = [title['item'] for title in borrowed_books_filter]

        if book_object.quantity > 0 and book_object.id not in borrowed_books:
            order_object.item = book_object
            order_object.customer = user_object
            order_object.save()
            book_object.quantity -= 1
            book_object.save()

    return redirect('/books/'+str(book_id))

