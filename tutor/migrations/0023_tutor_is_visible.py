# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-22 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0022_auto_20170715_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
