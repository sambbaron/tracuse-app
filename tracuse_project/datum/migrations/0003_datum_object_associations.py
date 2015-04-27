# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
        ('datum', '0002_foreign_key_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='datumobject',
            name='parent_associations_adjacent',
            field=models.ManyToManyField(related_name='child_associations_adjacent', through='association.AssociationAdjacent', to='datum.DatumObject'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='parent_associations_all',
            field=models.ManyToManyField(related_name='child_associations_all', through='association.AssociationAll', to='datum.DatumObject'),
        ),
    ]
