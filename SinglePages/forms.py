from django import forms
from .models import Comment
from django.forms import MultiWidget, TextInput, Textarea


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': TextInput(attrs={'size': 22, 'title': 'Your name', 'class': 'sm-form-control'}),
            'email': TextInput(attrs={'size': 22, 'title': 'Your name', 'class': 'sm-form-control'}),
            'body': Textarea(attrs={'cols': 58, 'rows': 7, 'tabindex': 4, 'class': 'sm-form-control'}),

        }
