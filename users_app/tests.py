from django.test import TestCase
from django.urls import reverse, resolve


class TestUrls(TestCase):
    def test_url_users_detail(self):
        path = reverse('user_account')
        assert resolve(path).view_name == 'user_account'
