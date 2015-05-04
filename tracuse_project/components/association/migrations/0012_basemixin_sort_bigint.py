# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0011_basemixin_ordering_remove_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationadjacent',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='associationall',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='associationdirection',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='associationtype',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
    ]
