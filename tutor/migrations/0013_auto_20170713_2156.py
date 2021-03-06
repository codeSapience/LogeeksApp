# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-13 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0012_auto_20170713_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/tutor/'),
        ),
    ]
