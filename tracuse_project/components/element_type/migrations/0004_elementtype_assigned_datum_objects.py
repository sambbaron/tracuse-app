# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0004_datumobject_assigned_element_types'),
        ('element_type', '0003_rename_plural_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementtype',
            name='assigned_datum_objects',
            field=models.ManyToManyField(through='element_type.ElementTypeDatumObject', to='datum.DatumObject'),
        ),
    ]
