# Generated by Django 3.2.6 on 2021-08-30 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_firstpageservicemodel_taggedservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstpageservicemodel',
            name='tables',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='service.blocksforservicemodel', verbose_name='Таблицы'),
        ),
    ]
