# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-12 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0029_auto_20170905_2206'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentNotification',
        ),
    ]
