# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_value', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementvaluebinary',
            name='element_value',
            field=models.BinaryField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='elementvaluedatetime',
            name='element_value',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='elementvaluedecimal',
            name='element_value',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=10, blank=True),
        ),
        migrations.AlterField(
            model_name='elementvaluestring',
            name='element_value',
            field=models.CharField(null=True, blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='elementvaluetextdata',
            name='element_value',
            field=models.TextField(null=True, blank=True),
        ),
    ]
