# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0017_filterset_rules_m2m'),
        ('viewuse', '0007_remove_template_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewusefilter',
            name='filter_set',
        ),
        migrations.RemoveField(
            model_name='viewusefilter',
            name='viewuse_object',
        ),
        migrations.AddField(
            model_name='viewuseobject',
            name='filter_json',
            field=models.CharField(default='', null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='viewuseobject',
            name='filter_set',
            field=models.ForeignKey(null=True, blank=True, db_column='filter_set_id', to='filter.FilterSet', related_name='viewuse_filters'),
        ),
        migrations.DeleteModel(
            name='ViewuseFilter',
        ),
    ]
