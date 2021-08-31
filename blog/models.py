from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from ckeditor_uploader.fields import RichTextUploadingField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class TaggedPost(TaggedItemBase):
    content_object = models.ForeignKey('Post', on_delete=models.CASCADE)


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # body = models.TextField()
    body = RichTextUploadingField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='uploads/blog/')
    # добавление модели Менеджер публикации 1
    objects = models.Manager()  # Менеджер по умолчанию
    published = PublishedManager()  # Наш новый менеджер
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикация'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=self.slug)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    answer = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
