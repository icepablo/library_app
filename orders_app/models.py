from django.db import models

from django.contrib.auth.models import User
from books_app.models import Book


class Order(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
