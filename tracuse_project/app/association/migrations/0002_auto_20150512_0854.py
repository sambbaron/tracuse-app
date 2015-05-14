# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('datum', '0001_initial'),
        ('association', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='associationall',
            name='child_datum',
            field=models.ForeignKey(related_name='all_child_associations', to='datum.DatumObject', db_column='child_datum_id'),
        ),
        migrations.AddField(
            model_name='associationall',
            name='parent_datum',
            field=models.ForeignKey(related_name='all_parent_associations', to='datum.DatumObject', db_column='parent_datum_id'),
        ),
        migrations.AddField(
            model_name='associationadjacent',
            name='association_type',
            field=models.ForeignKey(related_name='associations_adjacent', to='association.AssociationType', db_column='association_type_id'),
        ),
        migrations.AddField(
            model_name='associationadjacent',
            name='child_datum',
            field=models.ForeignKey(related_name='adjacent_child_associations', to='datum.DatumObject', db_column='child_datum_id'),
        ),
        migrations.AddField(
            model_name='associationadjacent',
            name='parent_datum',
            field=models.ForeignKey(related_name='adjacent_parent_associations', to='datum.DatumObject', db_column='parent_datum_id'),
        ),
        migrations.AlterUniqueTogether(
            name='associationall',
            unique_together=set([('parent_datum', 'child_datum')]),
        ),
        migrations.AlterIndexTogether(
            name='associationall',
            index_together=set([('parent_datum', 'child_datum')]),
        ),
        migrations.AlterUniqueTogether(
            name='associationadjacent',
            unique_together=set([('parent_datum', 'child_datum')]),
        ),
        migrations.AlterIndexTogether(
            name='associationadjacent',
            index_together=set([('parent_datum', 'child_datum')]),
        ),
    ]
