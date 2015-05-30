# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0003_textfields_nullable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewusefilter',
            name='viewuse_arrangement',
        ),
        migrations.AddField(
            model_name='viewusefilter',
            name='viewuse_object',
            field=models.ForeignKey(to='viewuse.ViewuseObject', db_column='viewuse_object_id', related_name='viewuse_filters', default=1),
            preserve_default=False,
        ),
    ]
