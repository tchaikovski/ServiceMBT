from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import format_html
from django.urls import reverse
from django.utils import timezone

STATUS_CHOICES = [
    ('<i class="icon-realestate-washing-machine"></i>', 'Стиралка'),
    ('<i class="icon-realestate-window"></i>', 'Окно'),
    ('<i class="icon-realestate-tools"></i>', 'Инструменты'),
    ('<i class="icon-realestate-box"></i>', 'Коробки'),

]


class SinglePageModel(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование страницы')
    icon = models.CharField(choices=STATUS_CHOICES, max_length=250, default='Freshman', blank=True, verbose_name='Иконки')
    slug = models.SlugField(max_length=70, unique=True, verbose_name='Наименование урла')
    content = models.TextField(verbose_name='Текст статьи')
    body = RichTextUploadingField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def choices_icon(self):
        return format_html(
            self.icon
            # '<i class="icon-realestate-washing-machine"></i>',
            # self.color_code,
            # self.first_name,
            # self.last_name,
        )

    def get_absolute_url(self):
        return reverse('singlepage', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
