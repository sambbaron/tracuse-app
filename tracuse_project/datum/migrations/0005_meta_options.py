# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0004_datumtype_parent_associations_all'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datumgroup',
            options={'verbose_name': 'Datum Group'},
        ),
        migrations.AlterModelOptions(
            name='datumobject',
            options={'verbose_name': 'Datum'},
        ),
        migrations.AlterModelOptions(
            name='datumtype',
            options={'verbose_name': 'Datum Type'},
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='datum_group',
            field=models.ForeignKey(db_column='datum_group_id', to='datum.DatumGroup'),
        ),
    ]
