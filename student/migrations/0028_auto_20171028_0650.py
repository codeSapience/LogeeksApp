# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-28 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0027_student_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='diary',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
