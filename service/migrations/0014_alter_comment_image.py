# Generated by Django 3.2.6 on 2021-08-24 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_auto_20210824_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, upload_to='comment_uploads/'),
        ),
    ]
