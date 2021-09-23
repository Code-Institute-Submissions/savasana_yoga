from django.test import TestCase
from django.urls import reverse, resolve
from checkout.views import checkout, checkout_success, cache_checkout_data

# Create your tests here.

# Unit Testing Checkout App Urls

class TestUrls(TestCase):

    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)


    def test_checkout_url_checkout_success(self):
        url = reverse('checkout_success', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout_success)


    def test_checkout_url_cache_checkout_data(self):
        url = reverse('cache_checkout_data')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cache_checkout_data)

