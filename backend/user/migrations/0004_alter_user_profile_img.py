# Generated by Django 4.2.2 on 2023-07-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20230629_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='static/img/user_default.png', upload_to='profile_img/'),
        ),
    ]
