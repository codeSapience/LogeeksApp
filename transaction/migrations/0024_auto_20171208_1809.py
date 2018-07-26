# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-08 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0023_auto_20171208_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_number', models.CharField(max_length=7)),
                ('tutor_name', models.CharField(max_length=80)),
                ('transaction', models.CharField(max_length=10)),
                ('tutor_bank_account_name', models.CharField(max_length=80, verbose_name='Tutor Account Name')),
                ('tutor_bank_account_number', models.CharField(max_length=10, verbose_name='Tutor NUBAN')),
                ('payment_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='tutor_bank_account_name',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='tutor_bank_account_number',
        ),
    ]