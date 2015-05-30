# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0011_elementoperator_verbosename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementdatatype',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementdatatype',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementdatatype',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementdatumtype',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementdatumtype',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementdatumtype',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementoperator',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementoperator',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementoperator',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementoption',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementoption',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementoption',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementtype',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementtype',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='elementtype',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
    ]
