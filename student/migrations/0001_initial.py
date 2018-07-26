# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-14 02:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Gender', max_length=6)),
                ('phoneNumber', models.CharField(max_length=18)),
                ('address', models.CharField(max_length=90)),
                ('photo', models.ImageField(upload_to='media/students/')),
                ('verification', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
