# Generated by Django 3.0.7 on 2020-08-13 08:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20200813_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='users',
            new_name='created_by',
        ),
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 8, 27, 48, 14761, tzinfo=utc)),
        ),
    ]