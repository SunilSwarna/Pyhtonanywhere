# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-30 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_stock1_email1'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock1',
            name='priority',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='stock1',
            name='status',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
