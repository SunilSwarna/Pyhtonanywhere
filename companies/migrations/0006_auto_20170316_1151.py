# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-16 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='adhar_no',
            field=models.IntegerField(),
        ),
    ]
