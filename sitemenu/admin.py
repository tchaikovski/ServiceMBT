from django.contrib import admin

# Register your models here.

from .models import CallBack


@admin.register(CallBack)
class SinglePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'geo')
    # list_filter = ('name', 'geo')
    # # list_editable = ('choices_icon',)
    # ordering = ['name']
    # search_fields = ['name']

