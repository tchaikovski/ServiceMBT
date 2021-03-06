from django.contrib.postgres.operations import TrigramExtension
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm, SearchForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # results = Post.objects.annotate(search=SearchVector('title', 'body'),).filter(search=query)
            #  Добавляем поиск оп частоте совпадении
            # search_vector = SearchVector('title', 'body')
            # Без приоритета тайтла выше
            search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            # results = Post.objects.annotate(search=search_vector, rank=SearchRank(
            # search_vector, search_query)).filter(
            #     search=search_query).order_by('-rank') #  Без приоритета тайтла
            results = Post.objects.annotate(rank=SearchRank(search_vector, search_query)).filter(
                rank__gte=0.3).order_by('-rank')

    return render(request, 'blog/post/search.html', {'form': form, 'query': query, 'results': results})


# Рейтинг весов от A-D от 1, 0.4, 0,2 и 0,1 - rank__gte=0.3 ограничивает вывод с рангом выше 0,3


class TrigramExtensions(TrigramExtension):
    pass


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'blog/post/list.html'


def post_share(request, post_id):
    #  получение статьи по индификатору
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        #  Форма отправлена на сохранение
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # все поля прошли валидацию
            cd = form.cleaned_data
            # Отправка электронной почты
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'test@adressayta.ru', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    #  Если страница не является целым числом, возвращаем 1 страницу.

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    #  Если число больше то возвращаем последнюю страницу

    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts, 'tag': tag})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    #  Список активных коментов для статьи
    comments = post.comments.filter(active=True)
    new_comment = None
    # Формирвание списка похожих статей
    pos_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=pos_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:2]

    rel_posts = Post.published.filter(tags__in=pos_tags_ids).exclude(id=post.id)
    rel_posts = rel_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', 'publish')[:4]

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
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment,
                                                     'comment_form': comment_form, 'similar_posts': similar_posts, 'rel_posts': rel_posts})
