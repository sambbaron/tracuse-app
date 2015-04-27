# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_value', '0002_values_nullable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementvaluebinary',
            name='element_option',
            field=models.ForeignKey(to='element_type.ElementOption', db_column='element_option_id', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='elementvalueboolean',
            name='element_option',
            field=models.ForeignKey(to='element_type.ElementOption', db_column='element_option_id', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='elementvaluedatetime',
            name='element_option',
            field=models.ForeignKey(to='element_type.ElementOption', db_column='element_option_id', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='elementvaluedecimal',
            name='element_option',
            field=models.ForeignKey(to='element_type.ElementOption', db_column='element_option_id', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='elementvaluestring',
            name='element_option',
            field=models.ForeignKey(to='element_type.ElementOption', db_column='element_option_id', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='elementvaluetextdata',
            name='element_option',
            field=models.ForeignKey(to='element_type.ElementOption', db_column='element_option_id', blank=True, null=True),
        ),
    ]
