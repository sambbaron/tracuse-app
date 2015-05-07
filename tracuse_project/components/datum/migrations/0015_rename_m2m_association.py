# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0013_rename_depth_distance'),
        ('datum', '0014_basemixin_sort_bigint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datumobject',
            name='adjacent_parent_datums',
        ),
        migrations.RemoveField(
            model_name='datumobject',
            name='all_parent_datums',
        ),
        migrations.AddField(
            model_name='datumobject',
            name='adjacent_child_datums',
            field=models.ManyToManyField(to='datum.DatumObject', related_name='adjacent_parent_datums', through='association.AssociationAdjacent'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='all_child_datums',
            field=models.ManyToManyField(to='datum.DatumObject', related_name='all_parent_datums', through='association.AssociationAll'),
        ),
    ]
