# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0004_elementtypedatumobject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementdatatype',
            options={'verbose_name': 'Element Data Type'},
        ),
        migrations.AlterModelOptions(
            name='elementoption',
            options={'verbose_name': 'Element Option'},
        ),
        migrations.AlterModelOptions(
            name='elementtypedatumobject',
            options={'verbose_name': 'Element Type'},
        ),
    ]
