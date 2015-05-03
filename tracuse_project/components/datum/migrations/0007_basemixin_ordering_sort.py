# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0006_datum_element_m2m_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datumobject',
            options={'ordering': ['sort'], 'verbose_name': 'Datum'},
        ),
    ]
