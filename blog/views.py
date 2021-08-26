from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from .forms import CommentForm



def view_blog(request):
    """ A view to return the blog page """

    blog_posts = Post.objects.filter(status=1).order_by('-created_on')

    context = {
        'blog_posts': blog_posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_post_detail(request, slug):
    """ A view to return an individual blog post """

    blog_post = get_object_or_404(Post, slug=slug)

    comments = blog_post.comments.filter(active=True)

    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = blog_post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    context = {
        'blog_post': blog_post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }

    return render(request, 'blog/blog_post_detail.html', context)
