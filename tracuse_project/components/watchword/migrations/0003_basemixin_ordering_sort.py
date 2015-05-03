# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchword', '0002_basemixin_ordering_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watchwordassociationtype',
            options={'verbose_name': 'Association Type Watchword', 'ordering': ('sort',)},
        ),
        migrations.AlterModelOptions(
            name='watchworddatumobject',
            options={'verbose_name': 'Datum Object Watchword', 'ordering': ('sort',)},
        ),
        migrations.AlterModelOptions(
            name='watchworddatumtype',
            options={'verbose_name': 'Datum Type Watchword', 'ordering': ('sort',)},
        ),
    ]
