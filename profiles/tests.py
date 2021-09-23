from django.test import TestCase
from django.urls import reverse, resolve
from profiles.views import profile, order_history

# Create your tests here.

# Unit Testing Profiles App Urls

class TestUrls(TestCase):

    def test_profiles_url_is_resolved(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)


    def test_profiles_url_order_history(self):
        url = reverse('order_history', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, order_history)
