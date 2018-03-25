# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testbase', '0010_auto_20180306_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_log',
            name='model_create',
        ),
        migrations.RemoveField(
            model_name='model_log',
            name='model_delete',
        ),
        migrations.RemoveField(
            model_name='model_log',
            name='model_edit',
        ),
        migrations.AddField(
            model_name='model_log',
            name='action',
            field=models.CharField(choices=[('СREATED', 'Created'), ('CHANGED', 'Changed'), ('DELETED', 'Deleted')], default='CHANGED', max_length=10),
        ),
        migrations.AddField(
            model_name='model_log',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Datetime'),
        ),
        migrations.AlterField(
            model_name='model_log',
            name='model_name',
            field=models.CharField(max_length=254, verbose_name='Name of model'),
        ),
    ]
