# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0007_m2m_verbose_and_str'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementtypedatumobject',
            options={'ordering': ['sort'], 'verbose_name': 'Datum Object - Element Type'},
        ),
        migrations.AlterModelOptions(
            name='elementtypedatumtype',
            options={'ordering': ['sort'], 'verbose_name': 'Datum Type - Element Type'},
        ),
    ]
