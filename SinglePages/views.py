from django.views.generic import ListView, DetailView
from .models import SinglePageModel, Comment
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm


def single_page_detail(request, post):
    post = get_object_or_404(SinglePageModel, slug=post)
    #  Список активных коментов для статьи
    comments = post.comments.filter(active=True)
    new_comment = None
    # template_name = get_object_or_404(SinglePageModel).temp_choices
    template_name = post.temp_choices
    # template_name = 'SinglePages/singlepagerepair.html'
    if request.method == 'POST':
        #  пользователь отправил коммент
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создаем комент но не записываем
            new_comment = comment_form.save(commit=False)
            # Привязываем комент к статье
            new_comment.post = post
            # Сохраняем комент
            new_comment.save()
            comment_form.save_m2m()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})

