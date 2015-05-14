# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('element_type', '0008_elementdatumtype_entitymixin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementdatatype',
            name='entity_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementdatatype',
            name='readable_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementdatatype',
            name='readable_plural_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementdatatype',
            name='schema_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementdatumtype',
            name='entity_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementdatumtype',
            name='readable_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementdatumtype',
            name='readable_plural_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementdatumtype',
            name='schema_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementoption',
            name='entity_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementoption',
            name='readable_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementoption',
            name='readable_plural_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementoption',
            name='schema_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementtype',
            name='entity_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementtype',
            name='readable_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementtype',
            name='readable_plural_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='elementtype',
            name='schema_name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
