# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0002_elementtypedatumtype_base_cols_remove'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementoption',
            name='element_type',
            field=models.ForeignKey(db_column='element_type_id', to='element_type.ElementType', related_name='element_options'),
        ),
        migrations.AlterField(
            model_name='elementtype',
            name='element_data_type',
            field=models.ForeignKey(db_column='element_data_type_id', to='element_type.ElementDataType', related_name='element_types'),
        ),
        migrations.AlterField(
            model_name='elementtypedatumtype',
            name='datum_type',
            field=models.ForeignKey(db_column='datum_type_id', to='datum.DatumType', related_name='element_types'),
        ),
        migrations.AlterField(
            model_name='elementtypedatumtype',
            name='element_type',
            field=models.ForeignKey(db_column='element_type_id', to='element_type.ElementType', related_name='datum_types'),
        ),
    ]
