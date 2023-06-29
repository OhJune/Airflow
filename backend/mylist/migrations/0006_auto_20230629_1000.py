# Generated by Django 3.1.1 on 2023-06-29 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mylist', '0005_auto_20230629_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='user',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='user_id'),
        ),
    ]
