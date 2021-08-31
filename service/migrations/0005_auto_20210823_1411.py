# Generated by Django 3.2.6 on 2021-08-23 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20210823_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blocksforservicemodel',
            options={'ordering': ['id'], 'verbose_name': 'Публикация табле', 'verbose_name_plural': 'Публикации табле'},
        ),
        migrations.RemoveField(
            model_name='blocksforservicemodel',
            name='cat',
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='tables',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='service.blocksforservicemodel', verbose_name='Таблицы'),
            preserve_default=False,
        ),
    ]