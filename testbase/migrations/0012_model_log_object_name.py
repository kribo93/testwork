# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testbase', '0011_auto_20180308_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_log',
            name='object_name',
            field=models.CharField(default=None, max_length=254, verbose_name='Odject'),
        ),
    ]
