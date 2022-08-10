# Generated by Django 2.2 on 2022-08-09 09:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20220804_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='name',
        ),
        migrations.AlterField(
            model_name='message',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 9, 9, 43, 19, 109644, tzinfo=utc)),
        ),
    ]
