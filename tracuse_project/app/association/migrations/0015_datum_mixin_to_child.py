# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0014_association_direction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationadjacent',
            name='child_datum',
            field=models.ForeignKey(related_name='adjacent_parent_associations', to='datum.DatumObject', db_column='child_datum_id'),
        ),
        migrations.AlterField(
            model_name='associationadjacent',
            name='parent_datum',
            field=models.ForeignKey(related_name='adjacent_child_associations', to='datum.DatumObject', db_column='parent_datum_id'),
        ),
        migrations.AlterField(
            model_name='associationall',
            name='child_datum',
            field=models.ForeignKey(related_name='all_parent_associations', to='datum.DatumObject', db_column='child_datum_id'),
        ),
        migrations.AlterField(
            model_name='associationall',
            name='parent_datum',
            field=models.ForeignKey(related_name='all_child_associations', to='datum.DatumObject', db_column='parent_datum_id'),
        ),
    ]
