from django import forms

from .models import blog_posts

class PostForm(forms.ModelForm):

    class Meta:
        model = blog_posts
        fields = ('title', 'tag', 'author')