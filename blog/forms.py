from django import forms 
from .models import Blog,Comment
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content','slug']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['content']