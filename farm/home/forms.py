from django import forms
from .models import Post

class HomeForm(forms.ModelForm):
    "to rewrite Text Input widget"
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder' : 'Write a post ...'
         }
    ))

    class Meta:
        model = Post
        fields = ('post',)
