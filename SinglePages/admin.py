from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode

from .models import SinglePageModel, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')



@admin.register(SinglePageModel)
class SinglePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'choices_icon')
    list_filter = ('name', 'slug')
    # list_editable = ('choices_icon',)
    ordering = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

    class Media:
        # js = ('js/admin/my_own_admin.js',)
        css = {
            'all': ('/static/demos/real-estate/css/font-icons.css',)
        }


