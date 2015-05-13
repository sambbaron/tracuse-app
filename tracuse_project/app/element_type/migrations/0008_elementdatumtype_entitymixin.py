# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0007_remove_field_usage'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementdatumtype',
            name='entity_name',
            field=models.CharField(db_index=True, max_length=25, default=''),
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='example',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='long_definition',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='readable_name',
            field=models.CharField(db_index=True, max_length=25, default=''),
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='readable_plural_name',
            field=models.CharField(max_length=25, default=''),
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='schema_name',
            field=models.CharField(max_length=25, default=''),
        ),
        migrations.AddField(
            model_name='elementdatumtype',
            name='short_definition',
            field=models.CharField(max_length=25, blank=True, null=True),
        ),
    ]
