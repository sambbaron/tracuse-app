# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementdatatype',
            name='plural_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='elementdatatype',
            name='readable_name',
            field=models.CharField(default='', max_length=25, db_index=True),
        ),
        migrations.AddField(
            model_name='elementdatatype',
            name='schema_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='elementoption',
            name='plural_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='elementoption',
            name='readable_name',
            field=models.CharField(default='', max_length=25, db_index=True),
        ),
        migrations.AddField(
            model_name='elementoption',
            name='schema_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='elementtype',
            name='plural_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='elementtype',
            name='readable_name',
            field=models.CharField(default='', max_length=25, db_index=True),
        ),
        migrations.AddField(
            model_name='elementtype',
            name='schema_name',
            field=models.CharField(default='', max_length=25),
        ),
    ]
