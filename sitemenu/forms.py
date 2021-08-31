from django.forms import ModelForm
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm

from .models import CallBack


class CallBackForm(ModelForm):
    class Meta:
        model = CallBack
        fields = "__all__"

        # fields = ['name', 'phone', 'geo', 'content']


# class SearchForm(forms.Form):
#     query = forms.CharField()
#

class BookModelForm(BSModalModelForm):
    class Meta:
        model = CallBack
        fields = ['name', 'phone', 'geo']
