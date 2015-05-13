# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0005_remove_field_usage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationdirection',
            name='entity_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='associationdirection',
            name='readable_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='associationdirection',
            name='readable_plural_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='associationdirection',
            name='schema_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='associationtype',
            name='entity_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='associationtype',
            name='readable_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='associationtype',
            name='readable_plural_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='associationtype',
            name='schema_name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
