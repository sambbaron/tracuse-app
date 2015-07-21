# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui_arrangement', '0001_initial'),
        ('ui_formatting', '0001_initial'),
        ('windowuse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='windowuseobject',
            name='ui_arrangement_type',
            field=models.ForeignKey(db_column='ui_arrangement_type_id', to='ui_arrangement.UiArrangementType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='windowuseobject',
            name='ui_formatting_type',
            field=models.ForeignKey(db_column='ui_formatting_type_id', to='ui_formatting.UiFormattingType', blank=True, null=True),
        ),
    ]
