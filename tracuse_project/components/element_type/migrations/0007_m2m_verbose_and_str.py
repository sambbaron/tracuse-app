# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0006_datum_element_m2m_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementtypedatumobject',
            options={'verbose_name': 'Datum Object - Element Type'},
        ),
        migrations.AlterModelOptions(
            name='elementtypedatumtype',
            options={'verbose_name': 'Datum Type - Element Type'},
        ),
    ]
