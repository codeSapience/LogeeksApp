# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-05 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0028_auto_20171028_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=18),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=image_cropping.fields.ImageCropField(blank=True, upload_to='media/tutor/'),
        ),
    ]