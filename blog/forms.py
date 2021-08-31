from django import forms
from .models import Comment
from django.forms import MultiWidget, TextInput, Textarea


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': TextInput(attrs={'size': 22, 'title': 'Your name', 'class': 'sm-form-control'}),
            'email': TextInput(attrs={'size': 22, 'title': 'Your name', 'class': 'sm-form-control'}),
            'body': Textarea(attrs={'cols': 58, 'rows': 7, 'tabindex': 4, 'class': 'sm-form-control'}),

        }


class SearchForm(forms.Form):
    query = forms.CharField()
