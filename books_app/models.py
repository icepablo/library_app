from django.db import models

from authors_app.models import Author


class Book(models.Model):
    title = models.TextField()
    quantity = models.IntegerField(default=None, null=True)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.title
