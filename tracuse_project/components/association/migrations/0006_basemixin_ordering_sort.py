# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0005_basemixin_ordering_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='associationadjacent',
            options={'verbose_name_plural': 'Associations Adjacent', 'verbose_name': 'Association Adjacent', 'ordering': ('sort',)},
        ),
        migrations.AlterModelOptions(
            name='associationall',
            options={'verbose_name_plural': 'Associations All', 'verbose_name': 'Association All', 'ordering': ('sort',)},
        ),
    ]
