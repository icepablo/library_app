from django.test import TestCase
from django.urls import reverse, resolve
from django.test import RequestFactory
from mixer.backend.django import mixer

from books_app.views import *


class TestUrls(TestCase):
    def test_url_detail(self):
        path = reverse('book_detail', kwargs={'book_id': 1})
        assert resolve(path).view_name == 'book_detail'

    def test_url_books(self):
        path = reverse('books')
        assert resolve(path).view_name == 'books'

    def test_view_home(self):
        path = reverse('home')
        request = RequestFactory().get(path)
        response=home(request)
        assert response.status_code == 200

    def test_view_books(self):
        path = reverse('books')
        request = RequestFactory().get(path)
        response = books(request)
        assert response.status_code == 200

    def test_view_detail(self):
        mixer.blend('books_app.Book')
        path = reverse('book_detail', kwargs={'book_id': 1})
        request = RequestFactory().get(path)
        response = book_detail(request, book_id=1)
        assert response.status_code == 200


