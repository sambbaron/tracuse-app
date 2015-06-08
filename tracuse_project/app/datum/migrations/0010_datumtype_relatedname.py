# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0009_entitymodel_names_nullable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datumtype',
            name='datum_group',
            field=models.ForeignKey(related_name='datum_types', db_column='datum_group_id', to='datum.DatumGroup'),
        ),
    ]
