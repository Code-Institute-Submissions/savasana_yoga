from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import view_blog, blog_post_detail, add_blog_post, edit_blog_post, delete_blog_post, comment_approve, comment_remove, edit_comment

# Create your tests here.

# Unit Testing Blog App Urls

class TestUrls(TestCase):

    def test_blog_url_is_resolved(self):
        url = reverse('view_blog')
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, view_blog)


    def test_blog_url_blog_post_detail(self):
        url = reverse('blog_post_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, blog_post_detail)


    def test_blog_url_add_blog_post(self):
        url = reverse('add_blog_post')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_blog_post)


    def test_blog_url_edit_blog_post(self):
        url = reverse('edit_blog_post', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_blog_post)


    def test_blog_url_delete_blog_post(self):
        url = reverse('delete_blog_post', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_blog_post)


    def test_blog_url_comment_approve(self):
        url = reverse('comment_approve', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, comment_approve)


    def test_blog_url_comment_remove(self):
        url = reverse('comment_remove', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, comment_remove)

    def test_blog_url_edit_comment(self):
        url = reverse('edit_comment', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_comment)


