from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post



def view_blog(request):
    """ A view to return the blog page """

    blog_posts = Post.objects.filter(status=1).order_by('-created_on')

    context = {
        'blog_posts': blog_posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_post_detail(request, blog_id):
    """ A view to return an individual blog post """

    blog_post = get_object_or_404(Post, pk=blog_id)

    context = {
        'blog_post': blog_post,
    }

    return render(request, 'blog/blog_post_detail.html', context)

