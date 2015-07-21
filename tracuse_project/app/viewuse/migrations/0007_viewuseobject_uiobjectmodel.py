# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui_arrangement', '0001_initial'),
        ('ui_formatting', '0001_initial'),
        ('viewuse', '0006_remove_viewusenested'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viewuseobject',
            options={'verbose_name': 'Viewuse Object', 'ordering': ['sort']},
        ),
        migrations.RemoveField(
            model_name='viewuseobject',
            name='viewuse_arrangement',
        ),
        migrations.RemoveField(
            model_name='viewuseobject',
            name='viewuse_datum',
        ),
        migrations.AddField(
            model_name='viewuseobject',
            name='ui_arrangement_type',
            field=models.ForeignKey(null=True, to='ui_arrangement.UiArrangementType', db_column='ui_arrangement_type_id', blank=True),
        ),
        migrations.AddField(
            model_name='viewuseobject',
            name='ui_formatting_type',
            field=models.ForeignKey(null=True, to='ui_formatting.UiFormattingType', db_column='ui_formatting_type_id', blank=True),
        ),
        migrations.DeleteModel(
            name='ViewuseArrangement',
        ),
        migrations.DeleteModel(
            name='ViewuseDatum',
        ),
    ]
