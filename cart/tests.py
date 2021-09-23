from django.test import TestCase
from django.urls import reverse, resolve
from cart.views import view_cart, add_to_cart, adjust_cart, remove_from_cart

# Create your tests here.

# Unit Testing Cart App Urls

class TestUrls(TestCase):

    def test_cart_url_is_resolved(self):
        url = reverse('view_cart')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_cart)


    def test_cart_url_add_to_cart(self):
        url = reverse('add_to_cart', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_to_cart)


    def test_cart_url_adjust_cart(self):
        url = reverse('adjust_cart', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, adjust_cart)


    def test_cart_url_remove_from_cart(self):
        url = reverse('remove_from_cart', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, remove_from_cart)

