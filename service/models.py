from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from ckeditor_uploader.fields import RichTextUploadingField


# from captcha.fields import CaptchaField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class TaggedService(TaggedItemBase):
    content_object = models.ForeignKey('ServiceModel', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория в модели")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория в модели'
        verbose_name_plural = 'Категории в модели'
        ordering = ['id']


class ServiceModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
    tables = models.ForeignKey('BlocksforServiceModel', on_delete=models.PROTECT, verbose_name="Таблицы")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_slug': self.slug})

    def get_absolute_url(self):
        return reverse('service', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Публикация в модели'
        verbose_name_plural = 'Публикации в модели'
        ordering = ['id']


class BlocksforServiceModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    price = models.TextField(blank=True, verbose_name="Блок с ценами")
    block_price = models.TextField(blank=True, verbose_name="Блок с расчетом стоимости")
    tab_price = models.TextField(blank=True, verbose_name="Таблица с ценами")
    block_one = models.TextField(blank=True, verbose_name="Блок после цены block_one")
    block_two = models.TextField(blank=True, verbose_name="Блок поломки block_two")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('block', kwargs={'block_slug': self.slug})

    class Meta:
        verbose_name = 'Модули для страниц'
        verbose_name_plural = 'Модули для страниц'
        ordering = ['id']


class Comment(models.Model):
    post = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name='comments')
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


class FirstPageServiceModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    tables = models.ForeignKey('BlocksforServiceModel', on_delete=models.PROTECT, verbose_name="Таблицы")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Главная страница в сервисе (страница категории)'
        verbose_name_plural = 'Главная страница в сервисе (страница категории)'
        ordering = ['id']
