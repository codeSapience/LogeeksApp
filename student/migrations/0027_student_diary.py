# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-27 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0026_auto_20171015_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='diary',
            field=models.CharField(default='No note yet', max_length=1000),
            preserve_default=False,
        ),
    ]