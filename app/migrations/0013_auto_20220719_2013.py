# Generated by Django 2.2 on 2022-07-19 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220719_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='userPlan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to=settings.AUTH_USER_MODEL),
        ),
    ]