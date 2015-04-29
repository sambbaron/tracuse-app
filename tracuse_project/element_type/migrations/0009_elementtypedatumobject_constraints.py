# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0008_elementtypedatumobject_constraints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementtypedatumobject',
            name='datum_object',
            field=models.ForeignKey(db_column='datum_object_id', to='datum.DatumObject', related_name='element_types_datum_objects'),
        ),
        migrations.AlterField(
            model_name='elementtypedatumobject',
            name='element_type',
            field=models.ForeignKey(db_column='element_type_id', to='element_type.ElementType', related_name='datum_objects_element_types'),
        ),
    ]
