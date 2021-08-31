from urllib import request
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
# from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from ServiceMBT.settings import GOOGLE_RECAPTCHA_SECRET_KEY, GOOGLE_RECAPTCHA_SITE_KEY
import urllib
import urllib.request
import urllib.error
import json
from .forms import *
from .models import *
from django.views.generic.edit import FormMixin
from .utils import *
from .forms import CommentForm
from .models import ServiceModel



def page_service_detail(request, post):
    post = get_object_or_404(ServiceModel, slug=post)
    #  Список активных коментов для статьи
    comments = post.comments.filter(active=True)
    new_comment = None
    # Формирвание списка похожих статей
    # pos_tags_ids = post.tags.values_list('id', flat=True)
    # similar_posts = ServiceModel.published.filter(tags__in=pos_tags_ids).exclude(id=post.id)
    # similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:2]

    # rel_posts = ServiceModel.published.filter(tags__in=pos_tags_ids).exclude(id=post.id)
    # rel_posts = rel_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', 'publish')[:4]

    if request.method == 'POST':
        #  пользователь отправил коммент
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.urlencode(values)
            req = urllib.Request(url, data)
            response = urllib.urlopen(req)
            result = json.load(response)
            ''' End reCAPTCHA validation '''

            # Создаем комент но не записываем
            new_comment = comment_form.save(commit=False)
            # Привязываем комент к статье
            new_comment.post = post
            # Сохраняем комент
            new_comment.save()
            comment_form.save_m2m()
    else:
        comment_form = CommentForm()

    return render(request, 'service/detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment,
                                                     'comment_form': comment_form, 'recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY})




class ServiceHome(DataMixin, ListView):
    model = ServiceModel
    template_name = 'uslugi/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return ServiceModel.objects.filter(is_published=True).select_related('cat')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class FirstPageServiceView(DetailView):
    model = FirstPageServiceModel
    context_object_name = 'first_page'
    template_name = 'service/first_detail.html'
    slug_url_kwarg = 'first_slug'



class ShowPost(DetailView):
    model = ServiceModel
    template_name = 'service/detail.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title=context['post'])
    #     # form = {'form': CommentForm()}
    #     return dict(list(context.items()) + list(c_def.items()))


class ServiceCategoryView(DataMixin, ListView):
    model = ServiceModel
    template_name = 'service/list.html'
    context_object_name = 'posts'
    slug_url_kwarg = 'post_slug'

    # allow_empty = False
    #
    def get_queryset(self):
        return ServiceModel.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')
    #
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))
