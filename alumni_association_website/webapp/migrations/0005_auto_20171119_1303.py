# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20171119_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='presenter',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='event',
            name='presenter_position',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]