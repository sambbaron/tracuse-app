# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0002_auto_20150707_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationall',
            name='child_datum',
            field=models.ForeignKey(related_name='all_parent_associations', db_column='child_datum_id', to='datum.DatumObject'),
        ),
        migrations.AlterField(
            model_name='associationall',
            name='parent_datum',
            field=models.ForeignKey(related_name='all_child_associations', db_column='parent_datum_id', to='datum.DatumObject'),
        ),
    ]
