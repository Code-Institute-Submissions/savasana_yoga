from django.test import TestCase, Client
from django.urls import reverse, resolve
from products.models import Product, Category
from home.views import index
import json

# Create your tests here.

# Unit Testing Home App Urls

class TestUrls(TestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)
        

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home.url = reverse('home')

    def test_home_GET(self):
        response = self.client.get(self.home.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
