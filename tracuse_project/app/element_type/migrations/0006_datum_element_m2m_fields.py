# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0006_datum_element_m2m_fields'),
        ('element_type', '0005_elementtype_assigned_datum_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementtype',
            name='assigned_datum_objects',
        ),
        migrations.RemoveField(
            model_name='elementtype',
            name='assigned_datum_types',
        ),
        migrations.AddField(
            model_name='elementtype',
            name='datum_objects',
            field=models.ManyToManyField(to='datum.DatumObject', related_name='+', through='element_type.ElementTypeDatumObject'),
        ),
        migrations.AddField(
            model_name='elementtype',
            name='datum_types',
            field=models.ManyToManyField(to='datum.DatumType', related_name='+', through='element_type.ElementTypeDatumType'),
        ),
    ]
