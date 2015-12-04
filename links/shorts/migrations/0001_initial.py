# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2000)),
                ('short', models.CharField(db_index=True, max_length=10)),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date published')),
                ('last_access_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='last accessed')),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ShortList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short', models.CharField(max_length=10)),
                ('in_use', models.BooleanField(default=False)),
            ],
        ),
    ]
