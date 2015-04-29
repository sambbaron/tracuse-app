# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0006_element_type_related_names'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementtypedatumobject',
            options={'verbose_name': 'Element Type - Datum Object'},
        ),
        migrations.AlterModelOptions(
            name='elementtypedatumtype',
            options={'verbose_name': 'Element Type - Datum Type'},
        ),
    ]
