# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0008_rename_str_expression_headline_expr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datumgroup',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='datumgroup',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='datumgroup',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
    ]
