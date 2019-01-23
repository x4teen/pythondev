from django import forms
from .models import PostModel


class PostModeForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content', 'author_email']
