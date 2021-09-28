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
    ('<i class="icon-realestate-box"></i>', 'Prim'),

]
TEMPLATE_CHOICES = [
    ('SinglePages/singlepage.html', 'All'),
    ('SinglePages/singlepagerepair.html', 'Ремонт шаблон'),
    ('SinglePages/contact.html', 'Страница контактов'),

]

#добавил мета и картинку

class SinglePageModel(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование страницы')
    # meta_title = models.CharField(max_length=250, blank=True, verbose_name='Мета тайтл')
    # meta_description = models.TextField(blank=True, verbose_name='мета описание')
    # meta_image = models.ImageField(blank=True, verbose_name='мета изображение', upload_to='uploads/')
    icon = models.CharField(choices=STATUS_CHOICES, max_length=250, blank=True, verbose_name='Иконки')
    slug = models.SlugField(max_length=70, unique=True, verbose_name='Наименование урла')
    content = models.TextField(verbose_name='Текст статьи')
    body = RichTextUploadingField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    temp_choices = models.CharField(max_length=500, choices=TEMPLATE_CHOICES, default='All')

    def __str__(self):
        return self.name

    def choices_icon(self):
        return format_html(
            self.icon
        )

    def get_absolute_url(self):
        return reverse('singlepage', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Comment(models.Model):
    post = models.ForeignKey(SinglePageModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    image = models.ImageField(blank=True, upload_to='comment_uploads/')
    answer = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
