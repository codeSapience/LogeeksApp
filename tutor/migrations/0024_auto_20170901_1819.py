# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-01 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0023_tutor_is_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='account_name',
            field=models.CharField(default='tutor_account_name', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='account_number',
            field=models.CharField(default='tutor_account_number', max_length=10),
            preserve_default=False,
        ),
    ]