from django.db import models


class Menu(models.Model):
    name = models.CharField('Название', max_length=100)
    url = models.CharField('Ссылка', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class CallBack(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=100)
    geo = models.CharField('Район города', max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    content = models.TextField(verbose_name='Заметки')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'