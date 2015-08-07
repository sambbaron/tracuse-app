# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0003_associationall_relatednames'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationadjacent',
            name='child_datum',
            field=models.ForeignKey(to='datum.DatumObject', related_name='adjacent_parent_associations', db_column='child_datum_id'),
        ),
        migrations.AlterField(
            model_name='associationadjacent',
            name='parent_datum',
            field=models.ForeignKey(to='datum.DatumObject', related_name='adjacent_child_associations', db_column='parent_datum_id'),
        ),
    ]
