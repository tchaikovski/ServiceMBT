# Generated by Django 3.2.6 on 2021-08-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_auto_20210823_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocksforservicemodel',
            name='block_one',
            field=models.TextField(blank=True, verbose_name='Блок после цены block_one'),
        ),
        migrations.AddField(
            model_name='blocksforservicemodel',
            name='block_two',
            field=models.TextField(blank=True, verbose_name='Блок поломки block_two'),
        ),
    ]