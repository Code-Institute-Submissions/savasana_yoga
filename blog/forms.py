from django import forms
from .widgets import CustomClearableFileInput
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'snippet', 'status', 'image_url', 'image')

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    