# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0006_entitymixin_increase_name_len'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationdirection',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='associationdirection',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='associationdirection',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='associationtype',
            name='readable_name',
            field=models.CharField(max_length=40, blank=True, db_index=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='associationtype',
            name='readable_plural_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='associationtype',
            name='schema_name',
            field=models.CharField(max_length=40, blank=True, null=True, default=''),
        ),
    ]
