# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-01 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_auto_20170803_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='student_id',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
