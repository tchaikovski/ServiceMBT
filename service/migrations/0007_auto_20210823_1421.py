# Generated by Django 3.2.6 on 2021-08-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_alter_blocksforservicemodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocksforservicemodel',
            name='block_price',
            field=models.CharField(default=1, max_length=255, verbose_name='Блок с расчетом стоимости'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blocksforservicemodel',
            name='price',
            field=models.TextField(blank=True, verbose_name='Блок с ценами'),
        ),
        migrations.AddField(
            model_name='blocksforservicemodel',
            name='tab_price',
            field=models.TextField(blank=True, verbose_name='Таблица с ценами'),
        ),
    ]
