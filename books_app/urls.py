from django.urls import path

import books_app.views


urlpatterns = [
    path('', books_app.views.books, name='books'),
    path('<int:book_id>/', books_app.views.book_detail, name='book_detail'),
    path('<int:book_id>/borrow', books_app.views.borrow, name='borrow'),

]
