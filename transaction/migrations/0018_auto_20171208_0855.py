# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-08 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0017_auto_20171115_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tutor_payment',
            field=models.FloatField(editable=False),
        ),
    ]
