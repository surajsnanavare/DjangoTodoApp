# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-05 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_title', models.CharField(max_length=50)),
                ('todo_note', models.CharField(max_length=500)),
            ],
        ),
    ]
