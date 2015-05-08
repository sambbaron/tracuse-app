# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0015_datum_mixin_to_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationadjacent',
            name='child_datum',
            field=models.ForeignKey(to='datum.DatumObject', related_name='adjacent_child_associations', db_column='child_datum_id'),
        ),
        migrations.AlterField(
            model_name='associationadjacent',
            name='parent_datum',
            field=models.ForeignKey(to='datum.DatumObject', related_name='adjacent_parent_associations', db_column='parent_datum_id'),
        ),
        migrations.AlterField(
            model_name='associationall',
            name='child_datum',
            field=models.ForeignKey(to='datum.DatumObject', related_name='all_child_associations', db_column='child_datum_id'),
        ),
        migrations.AlterField(
            model_name='associationall',
            name='parent_datum',
            field=models.ForeignKey(to='datum.DatumObject', related_name='all_parent_associations', db_column='parent_datum_id'),
        ),
    ]
