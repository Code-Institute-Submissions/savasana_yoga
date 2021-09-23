from django.test import TestCase, Client
from django.urls import reverse, resolve
from products.models import Product, Category
from products.views import all_products, product_info, add_product, edit_product, delete_product, view_timetable
import json

# Create your tests here.

# Unit Testing Products App Urls

class TestUrls(TestCase):

    def test_products_url_is_resolved(self):
        url = reverse('products')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_products)


    def test_products_url_product_detail(self):
        url = reverse('product_info', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_info)


    def test_products_url_add_product(self):
        url = reverse('add_product')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_product)


    def test_products_url_edit_product(self):
        url = reverse('edit_product', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_product)


    def test_products_url_delete_product(self):
        url = reverse('delete_product', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_product)


    def test_products_url_timetable(self):
        url = reverse('view_timetable')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_timetable)


# Testing Products Views


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.products_url = reverse('products')
        self.product_info_url = reverse('product_info', args=[1])
        Product.objects.create(
            name='testproduct',
            day='1',
            description='a testing description for a product',
            price=20,
            number_of_sessions=5,
        )

    def test_all_products_GET(self):
        response = self.client.get(self.products_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_info_GET(self):
        response = self.client.get(self.product_info_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_info.html')


class TestModels(TestCase):

    def setUp(self):
        self.testproduct = Product.objects.create(
            name='testproduct',
            day='1',
            description='a testing description for a product',
            tagline='a test tagline',
            price=20,
            number_of_sessions=5,
        )

    def test_product_returns_name(self):
        self.assertEquals(self.testproduct.name, 'testproduct')

    def test_product_category_returns_friendly_name(self):
        self.testcategory = Category.objects.create(
            product=self.testproduct,
            name='testing_category',
        )
        self.assertEquals(self.testcategory.name, 'testing_category')