# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0003_rename_plural_name'),
        ('datum', '0003_rename_plural_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='datumobject',
            name='assigned_element_types',
            field=models.ManyToManyField(through='element_type.ElementTypeDatumObject', to='element_type.ElementType'),
        ),
    ]
