# Generated by Django 3.0.7 on 2020-08-13 12:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20200813_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 12, 24, 29, 871758, tzinfo=utc)),
        ),
    ]
