# Generated by Django 2.2 on 2022-07-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20220723_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='repository_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]