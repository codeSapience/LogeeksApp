# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-08 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0028_auto_20171208_0755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='account_number',
            new_name='bank_account_number',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='account_name',
        ),
        migrations.AddField(
            model_name='tutor',
            name='bank_account_name',
            field=models.CharField(default='tutor_bank_account_name', max_length=80),
            preserve_default=False,
        ),
    ]
