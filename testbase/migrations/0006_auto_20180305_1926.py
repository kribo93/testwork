# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 19:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testbase', '0005_auto_20180301_0845'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Study_Group',
            new_name='Group',
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'group', 'verbose_name_plural': 'groups'},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='groupe',
            new_name='in_group',
        ),
    ]