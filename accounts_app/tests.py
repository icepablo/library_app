from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve

from django.contrib.auth.models import User


class TestUrls(TestCase):
    def test_url_login(self):
        path = reverse('login')
        assert resolve(path).view_name == 'login'

    def test_url_logout(self):
        path = reverse('logout')
        assert resolve(path).view_name == 'logout'

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        client = Client()
        is_logged = client.login(username='testuser', password='secret')
        self.assertTrue(is_logged)

