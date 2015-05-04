# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0009_basemixin_ordering_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='associationadjacent',
            options={'ordering': ['sort', '__str__'], 'verbose_name_plural': 'Associations Adjacent', 'verbose_name': 'Association Adjacent'},
        ),
        migrations.AlterModelOptions(
            name='associationall',
            options={'ordering': ['sort', '__str__'], 'verbose_name_plural': 'Associations All', 'verbose_name': 'Association All'},
        ),
    ]
