# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0009_basemixin_ordering_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementtypedatumobject',
            options={'verbose_name': 'Datum Object - Element Type', 'ordering': ('-sort',)},
        ),
        migrations.AlterModelOptions(
            name='elementtypedatumtype',
            options={'verbose_name': 'Datum Type - Element Type', 'ordering': ('-sort',)},
        ),
    ]
