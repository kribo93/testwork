# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testbase', '0002_auto_20180228_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='study_group',
            name='course_leader',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='testbase.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='card_number',
            field=models.PositiveIntegerField(unique=True, verbose_name='card number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='groupe',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='testbase.Study_Group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='study_group',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='name of group'),
        ),
    ]
