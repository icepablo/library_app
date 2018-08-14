from django.contrib import admin
from django.urls import path,include

import books_app.views


urlpatterns = [
    path('home/', books_app.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('books/', include('books_app.urls'), name='book'),
    path('authors/', include('authors_app.urls'), name='authors'),
    path('accounts/', include('accounts_app.urls'), name='accounts'),
    path('users/', include('users_app.urls'), name='users'),
]
