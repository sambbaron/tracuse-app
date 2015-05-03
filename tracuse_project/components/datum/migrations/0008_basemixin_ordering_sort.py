# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0007_basemixin_ordering_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datumobject',
            options={'verbose_name': 'Datum', 'ordering': ('sort',)},
        ),
    ]
