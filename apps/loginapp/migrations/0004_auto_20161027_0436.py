# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_auto_20161027_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(max_length=1000),
        ),
    ]