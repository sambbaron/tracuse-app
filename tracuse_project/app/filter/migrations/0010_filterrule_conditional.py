# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0009_filter_set_related_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterruleassociation',
            name='conditional',
            field=models.CharField(choices=[('AND', 'AND'), ('OR', 'OR')], default='AND', null=True, max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='filterruleelement',
            name='conditional',
            field=models.CharField(choices=[('AND', 'AND'), ('OR', 'OR')], default='AND', null=True, max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='filterrulegroup',
            name='conditional',
            field=models.CharField(choices=[('AND', 'AND'), ('OR', 'OR')], default='AND', null=True, max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='filterruletype',
            name='conditional',
            field=models.CharField(choices=[('AND', 'AND'), ('OR', 'OR')], default='AND', null=True, max_length=3, blank=True),
        ),
    ]
