# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0014_basemixin_ordering_remove_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementdatatype',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='elementoption',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='elementtype',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='elementtypedatumobject',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='elementtypedatumtype',
            name='sort',
            field=models.BigIntegerField(default=0, db_index=True),
        ),
    ]
