# Generated by Django 3.2.6 on 2021-08-23 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_delete_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicemodel',
            old_name='title',
            new_name='name',
        ),
        migrations.CreateModel(
            name='BlocksforServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.servicemodel', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Публикация в модели',
                'verbose_name_plural': 'Публикации в модели',
                'ordering': ['id'],
            },
        ),
    ]
