# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
        ('datum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='associationall',
            name='child_datum',
            field=models.ForeignKey(db_column='child_datum_id', related_name='+', to='datum.DatumObject'),
        ),
        migrations.AddField(
            model_name='associationall',
            name='parent_datum',
            field=models.ForeignKey(db_column='parent_datum_id', related_name='+', to='datum.DatumObject'),
        ),
        migrations.AddField(
            model_name='associationadjacent',
            name='association_type',
            field=models.ForeignKey(db_column='association_type_id', related_name='associations_adjacent', to='association.AssociationType'),
        ),
        migrations.AddField(
            model_name='associationadjacent',
            name='child_datum',
            field=models.ForeignKey(db_column='child_datum_id', related_name='+', to='datum.DatumObject'),
        ),
        migrations.AddField(
            model_name='associationadjacent',
            name='parent_datum',
            field=models.ForeignKey(db_column='parent_datum_id', related_name='+', to='datum.DatumObject'),
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
