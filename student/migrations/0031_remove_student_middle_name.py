# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-13 01:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0030_delete_studentnotification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='middle_name',
        ),
    ]