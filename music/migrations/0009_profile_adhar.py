# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-27 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20170124_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Adhar',
            field=models.CharField(default='1234-5678-9012', max_length=14),
        ),
    ]
