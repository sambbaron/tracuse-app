# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_value', '0008_basemixin_ordering_remove_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementvaluebinary',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='elementvalueboolean',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='elementvaluedatetime',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='elementvaluedecimal',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='elementvaluestring',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='elementvaluetextdata',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
    ]
