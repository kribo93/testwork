# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-01 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbase', '0004_auto_20180228_0813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
        migrations.AlterModelOptions(
            name='study_group',
            options={'verbose_name': 'study_group', 'verbose_name_plural': 'study_groups'},
        ),
    ]