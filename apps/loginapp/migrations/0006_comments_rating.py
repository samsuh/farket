# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0005_comments_comment_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
