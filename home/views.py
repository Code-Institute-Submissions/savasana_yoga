from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.


def index(request):
    """ A view to return the index page """
    posts = Post.objects.order_by('-created_on')[0:1]

    context = {
        'posts': posts,
    }

    return render(request, 'home/index.html', context)

