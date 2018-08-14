from django.db import models


class Author(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
