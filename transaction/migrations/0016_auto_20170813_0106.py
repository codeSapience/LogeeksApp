# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-13 00:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0015_auto_20170813_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['date_initialized']},
        ),
    ]
