# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-19 04:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0009_auto_20170608_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 6, 19, 4, 41, 46, 535809, tzinfo=utc))),
                ('related_transaction', models.CharField(max_length=10)),
                ('message_title', models.CharField(max_length=50)),
                ('message_content', models.CharField(max_length=1000)),
                ('read_status', models.BooleanField(default=False)),
                ('notification_tag', models.CharField(max_length=20)),
            ],
        ),
    ]
