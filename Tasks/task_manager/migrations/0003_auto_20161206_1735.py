# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_auto_20161206_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]