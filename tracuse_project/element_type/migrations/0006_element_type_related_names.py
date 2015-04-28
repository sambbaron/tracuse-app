# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0005_meta_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementtypedatumobject',
            name='datum_object',
            field=models.ForeignKey(to='datum.DatumObject', db_column='datum_object_id', related_name='element_types_datum_objects'),
        ),
        migrations.AlterField(
            model_name='elementtypedatumobject',
            name='element_type',
            field=models.ForeignKey(to='element_type.ElementType', db_column='element_type_id', related_name='datum_objects_element_types'),
        ),
        migrations.AlterField(
            model_name='elementtypedatumtype',
            name='datum_type',
            field=models.ForeignKey(to='datum.DatumType', db_column='datum_type_id', related_name='element_types_datum_types'),
        ),
        migrations.AlterField(
            model_name='elementtypedatumtype',
            name='element_type',
            field=models.ForeignKey(to='element_type.ElementType', db_column='element_type_id', related_name='datum_types_element_types'),
        ),
    ]
