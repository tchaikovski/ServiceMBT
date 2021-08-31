from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import CallBack

from .forms import CallBackForm


def page_not_found_view(request, exception):
    return render(request, 'errs/404.html', status=404)


def page403_not_found_view(request, exception):
    return render(request, 'errs/403.html', status=403)


# def page500_not_found_view(request, exception):
#     return render(request, 'errs/500.html', status=500)
