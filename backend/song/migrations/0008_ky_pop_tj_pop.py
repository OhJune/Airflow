# Generated by Django 3.1.1 on 2023-06-17 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0007_auto_20230616_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='tj_pop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=30)),
                ('cmp', models.CharField(max_length=30)),
                ('writer', models.CharField(max_length=30)),
                ('tj_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tjpop_set', to='song.tjsong')),
            ],
        ),
        migrations.CreateModel(
            name='ky_pop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=30)),
                ('cmp', models.CharField(max_length=30)),
                ('writer', models.CharField(max_length=30)),
                ('ky_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kypop_set', to='song.kysong')),
            ],
        ),
    ]
