from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# from captcha.fields import CaptchaField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

from django.forms import TextInput, Textarea

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = ServiceModel
        fields = ['name', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['name']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # captcha = CaptchaField()


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)

    class Meta:
        model = Comment
        # fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'size': 22, 'placeholder': 'Ваше Имя', 'title': 'Your name', 'class': 'sm-form-control'}),
            'email': TextInput(attrs={'size': 22, 'placeholder': 'E-Mail для связи', 'title': 'Your email', 'class': 'sm-form-control'}),
            'body': Textarea(attrs={'cols': 58, 'placeholder': 'Вопрос', 'rows': 7, 'tabindex': 4, 'class': 'sm-form-control'}),

        }

        fields = ('name', 'email', 'body')

