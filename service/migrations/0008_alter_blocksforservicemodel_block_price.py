# Generated by Django 3.2.6 on 2021-08-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20210823_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocksforservicemodel',
            name='block_price',
            field=models.CharField(blank=True, max_length=255, verbose_name='Блок с расчетом стоимости'),
        ),
    ]