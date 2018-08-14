from django.test import TestCase
from django.urls import reverse, resolve
from django.test import RequestFactory
from mixer.backend.django import mixer

from authors_app.views import *


class TestUrls(TestCase):
    def test_url_detail2(self):
        path = reverse('author_detail', kwargs={'author_id': 1})
        assert resolve(path).view_name == 'author_detail'

    def test_url_authors(self):
        path = reverse('authors')
        assert resolve(path).view_name == 'authors'

    def test_view_authors(self):
        path = reverse('authors')
        request = RequestFactory().get(path)
        response = authors(request)
        assert response.status_code == 200

    def test_view_detail(self):
        mixer.blend('authors_app.Author')
        path = reverse('author_detail', kwargs={'author_id': 1})
        request = RequestFactory().get(path)
        response = author_detail(request, author_id=1)
        assert response.status_code == 200
