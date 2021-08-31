from django import template
from sitemenu.models import Menu
from SinglePages.models import SinglePageModel
from blog.models import Post
from sitemenu.forms import CallBackForm


register = template.Library()


def func_chunks_generators(lst, n):
    """ Функция деления объекта на группы - разбиение списка """
    for i in range(0, len(lst), n):
        yield lst[i: i + n]

# Формирование второго меню в шаблоне одиночных страниц
@register.inclusion_tag('SinglePages/singlemenu.html', takes_context=True)
def show_top_menu(context):
    single_menu = SinglePageModel.objects.all()
    return {
        "single_menu": single_menu,
    }

# Формирование меню из одиночных страниц
@register.inclusion_tag('header.html', takes_context=True)
def show_header_menu(context):
    """ Формирование меню из одиночных страниц """
    objects = SinglePageModel.objects.all()
    blog_objects = Post.objects.all()
    menu_items = func_chunks_generators(objects, 1)  # цифра перед )) означает по сколько анкоров в меню выводить в столбике
    return {
        'menu_items': menu_items, 'blog_objects': blog_objects
    }

