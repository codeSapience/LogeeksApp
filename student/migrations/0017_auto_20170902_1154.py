# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-02 10:54
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_auto_20170902_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('photo', '530x530', adapt_rotation=False, allow_fullsize=True, free_crop=True, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping'),
        ),
    ]
