# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-15 11:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0016_auto_20170813_0106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-date_initialized']},
        ),
    ]
