# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-02 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_auto_20170902_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='cropping',
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to='media/student/'),
        ),
    ]
