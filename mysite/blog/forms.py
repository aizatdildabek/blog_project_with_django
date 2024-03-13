from django import forms
from .models import Post, Comment


class CreatePostForm(forms.ModelForm):
    # title = forms.CharField(label='Title')
    # content = forms.CharField(label='Content')

    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        # fields = ['title', 'content', 'author', 'categories']
        # fields = '__all__'
        # exclude = ['created_at', 'updated_at']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']