from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
        widgets = {
            'summary': forms.Textarea(attrs={'rows':3}),
            'content': forms.Textarea(attrs={'rows':8}),
        }
