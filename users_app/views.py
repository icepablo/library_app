from django.shortcuts import render, get_object_or_404,redirect

from django.contrib.auth.models import User
from books_app.models import Book
from orders_app.models import Order


def user_account(request):
    user_object = User.objects.get(id=request.user.id)
    user_orders = Order.objects.filter(customer__exact=user_object)
    return render(request,'users_app/user_account.html',{'orders':user_orders})


def give_back(request, order_id):
    delete_order = get_object_or_404(Order, pk=order_id)
    book_object = get_object_or_404(Book, pk=delete_order.item.id)
    book_object.quantity += 1
    book_object.save()
    delete_order.delete()
    return redirect('/users/'+str('my_account'))
