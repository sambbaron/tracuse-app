# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0005_elementtype_assigned_datum_types'),
        ('datum', '0005_datumtype_assigned_element_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datumobject',
            name='assigned_element_types',
        ),
        migrations.RemoveField(
            model_name='datumtype',
            name='assigned_element_types',
        ),
        migrations.AddField(
            model_name='datumobject',
            name='element_types',
            field=models.ManyToManyField(to='element_type.ElementType', related_name='+', through='element_type.ElementTypeDatumObject'),
        ),
        migrations.AddField(
            model_name='datumtype',
            name='element_types',
            field=models.ManyToManyField(to='element_type.ElementType', related_name='+', through='element_type.ElementTypeDatumType'),
        ),
    ]
