# Generated by Django 3.1.1 on 2023-06-16 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0005_auto_20230616_1152'),
        ('mylist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='ky_number',
            field=models.ForeignKey(db_column='ky_number', on_delete=django.db.models.deletion.CASCADE, related_name='mylist_set', to='song.kysong'),
        ),
        migrations.AlterField(
            model_name='mylist',
            name='tj_number',
            field=models.ForeignKey(db_column='tj_number', on_delete=django.db.models.deletion.CASCADE, related_name='mylist_set', to='song.tjsong'),
        ),
    ]
