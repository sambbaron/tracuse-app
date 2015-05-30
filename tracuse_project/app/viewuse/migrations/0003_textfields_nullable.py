# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0002_initial2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewusefilter',
            name='filter_json',
            field=models.CharField(blank=True, max_length=255, default='', null=True),
        ),
        migrations.AlterField(
            model_name='viewusefilter',
            name='filter_set',
            field=models.ForeignKey(blank=True, null=True, related_name='viewuse_filters', to='filter.FilterSet', db_column='filter_set_id'),
        ),
    ]
