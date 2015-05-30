# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0004_viewusefilter_to_viewuseobject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewusearrangement',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='viewusearrangement',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='viewusearrangement',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='viewusedatum',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='viewusedatum',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='viewusedatum',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='viewusefilter',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='viewusefilter',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='viewusefilter',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='viewuseobject',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='viewuseobject',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='viewuseobject',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
    ]
