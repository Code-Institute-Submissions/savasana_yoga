from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm, PostForm


def view_blog(request):
    """ A view to return the blog page """

    blog_posts = Post.objects.order_by('-created_on')

    context = {
        'blog_posts': blog_posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_post_detail(request, blog_post_id):
    """ A view to return an individual blog post """

    blog_post = get_object_or_404(Post, pk=blog_post_id)

    awaiting_approval_comments = blog_post.comments.filter(approved_comment=False)

    comments = blog_post.comments.filter(approved_comment=True)

    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = blog_post
            # Assign the user in session as the comment author
            new_comment.author = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    context = {
        'blog_post': blog_post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'awaiting_approval_comments': awaiting_approval_comments,
    }

    return render(request, 'blog/blog_post_detail.html', context)


@login_required
def add_blog_post(request):
    """ Add a post to the blog """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('blog_post_detail', args=[blog_post.id]))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()
     
    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog_post(request, blog_post_id):
    """
    Edit a blog post.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(Post, pk=blog_post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('blog_post_detail', args=[blog_post.id]))
        else:
            messages.error(
                    request,
                    'Failed to update the blog post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=blog_post)
        messages.info(request, f'You are editing {blog_post.title}')

    template = 'blog/edit_blog_post.html'
    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, template, context)


@login_required
def delete_blog_post(request, blog_post_id):

    blog_post = get_object_or_404(Post, pk=blog_post_id)

    if request.user == blog_post.author or request.user.is_superuser:
        blog_post.delete()
        messages.success(request, 'Blog Post deleted!')
        return redirect(reverse('view_blog'))

    else:

        messages.error(request, 'You cannot do that !')
        return redirect(reverse('view_blog'))


@login_required
def comment_approve(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user.is_superuser:
        comment.approve()
        messages.success(request, 'Comment has been approved!')
        return redirect(reverse('view_blog'))

    else:
        messages.error(request, 'You do not have access to approve comments!')
        return redirect('view_blog')


@login_required
def comment_remove(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Your comment is deleted !')
        return redirect(reverse('view_blog'))

    else:

        messages.error(request, 'It is not possible to delete comments you did not create!')
        return redirect(reverse('view_blog'))

