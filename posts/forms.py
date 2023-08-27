from django import forms
from posts.models import Commets, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commets
        fields = ("name", "text")
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")