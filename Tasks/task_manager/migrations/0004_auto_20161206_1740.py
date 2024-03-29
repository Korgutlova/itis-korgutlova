# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 14:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0003_auto_20161206_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('T', 'To Do'), ('P', 'In Progress'), ('R', 'Review'), ('D', 'Done')], default='T', max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime.today, null=True),
        ),
    ]
