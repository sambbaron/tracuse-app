# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0004_elementtype_assigned_datum_objects'),
        ('datum', '0004_datumobject_assigned_element_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='datumtype',
            name='assigned_element_types',
            field=models.ManyToManyField(through='element_type.ElementTypeDatumType', to='element_type.ElementType'),
        ),
    ]
