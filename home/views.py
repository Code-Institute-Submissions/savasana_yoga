from django.shortcuts import render, get_object_or_404
from blog.models import Post
from products.models import Product, Category

# Create your views here.


def index(request):
    """ A view to return the index page """
    posts = Post.objects.order_by('-created_on')[0:1]
    products = Product.objects.filter(category__name='beginner_class')[0:3]
    context = {
        'posts': posts,
        'products': products,
    }

    return render(request, 'home/index.html', context)

