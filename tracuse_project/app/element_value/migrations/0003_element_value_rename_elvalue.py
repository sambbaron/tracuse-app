# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('element_value', '0002_element_value_boolean_default_false'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elementvaluebinary',
            old_name='element_value',
            new_name='elvalue',
        ),
        migrations.RenameField(
            model_name='elementvalueboolean',
            old_name='element_value',
            new_name='elvalue',
        ),
        migrations.RenameField(
            model_name='elementvaluedatetime',
            old_name='element_value',
            new_name='elvalue',
        ),
        migrations.RenameField(
            model_name='elementvaluedecimal',
            old_name='element_value',
            new_name='elvalue',
        ),
        migrations.RenameField(
            model_name='elementvaluestring',
            old_name='element_value',
            new_name='elvalue',
        ),
        migrations.RenameField(
            model_name='elementvaluetextdata',
            old_name='element_value',
            new_name='elvalue',
        ),
    ]
