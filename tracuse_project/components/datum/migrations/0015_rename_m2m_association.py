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
            name='parent_associations_adjacent',
        ),
        migrations.RemoveField(
            model_name='datumobject',
            name='parent_associations_all',
        ),
        migrations.AddField(
            model_name='datumobject',
            name='child_associations_adjacent',
            field=models.ManyToManyField(to='datum.DatumObject', related_name='parent_associations_adjacent', through='association.AssociationAdjacent'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='child_associations_all',
            field=models.ManyToManyField(to='datum.DatumObject', related_name='parent_associations_all', through='association.AssociationAll'),
        ),
    ]
