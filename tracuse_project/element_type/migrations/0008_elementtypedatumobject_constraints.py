# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0007_elementtype_meta_verbose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementtypedatumobject',
            name='datum_object',
            field=models.ForeignKey(related_name='element_types_datum_objects', db_constraint=False, to='datum.DatumObject', db_column='datum_object_id'),
        ),
        migrations.AlterField(
            model_name='elementtypedatumobject',
            name='element_type',
            field=models.ForeignKey(related_name='datum_objects_element_types', db_constraint=False, to='element_type.ElementType', db_column='element_type_id'),
        ),
    ]
