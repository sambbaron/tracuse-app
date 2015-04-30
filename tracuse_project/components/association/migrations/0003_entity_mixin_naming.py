# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0002_auto_20150429_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='associationdirection',
            name='plural_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='associationdirection',
            name='readable_name',
            field=models.CharField(default='', max_length=25, db_index=True),
        ),
        migrations.AddField(
            model_name='associationdirection',
            name='schema_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='associationtype',
            name='plural_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='associationtype',
            name='readable_name',
            field=models.CharField(default='', max_length=25, db_index=True),
        ),
        migrations.AddField(
            model_name='associationtype',
            name='schema_name',
            field=models.CharField(default='', max_length=25),
        ),
    ]
