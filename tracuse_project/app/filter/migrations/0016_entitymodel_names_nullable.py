# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0015_filterruledatatype_filtersetdatatyperule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterset',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='filterset',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='filterset',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
    ]
