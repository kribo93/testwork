# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testbase', '0012_model_log_object_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='course_leader',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='testbase.Student'),
        ),
    ]
