# Generated by Django 3.2.6 on 2021-08-24 20:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SinglePages', '0003_alter_singlepagemodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlepagemodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 24, 20, 0, 30, 76060, tzinfo=utc)),
        ),
    ]
