# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0005_datumtype_assigned_element_types'),
        ('element_type', '0004_elementtype_assigned_datum_objects'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementtype',
            name='assigned_datum_types',
            field=models.ManyToManyField(through='element_type.ElementTypeDatumType', to='datum.DatumType'),
        ),
    ]
