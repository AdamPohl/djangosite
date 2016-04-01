from django import forms
from .models import Post, Nform

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('answer',)
