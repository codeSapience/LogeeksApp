# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-25 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0026_auto_20170905_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutornotification',
            name='notification_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
