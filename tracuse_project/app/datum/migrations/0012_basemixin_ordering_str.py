# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0011_basemixin_ordering_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datumobject',
            options={'ordering': ['sort', '__str__'], 'verbose_name': 'Datum'},
        ),
    ]
