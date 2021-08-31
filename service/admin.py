from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_create', 'get_html_photo', 'is_published', 'id')
    list_display_links = ('name',)
    search_fields = ('name', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("name",)}
    # fields = ('name', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class BlocksforServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'answer')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(ServiceModel, PagesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlocksforServiceModel, BlocksforServiceAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.site_title = 'Админ-панель сайта'
admin.site.site_header = 'Админ-панель'


# FirstPageServiceModel