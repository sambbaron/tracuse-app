# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0004_rename_plural_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='associationadjacent',
            options={'verbose_name': 'Association Adjacent', 'ordering': ['sort'], 'verbose_name_plural': 'Associations Adjacent'},
        ),
        migrations.AlterModelOptions(
            name='associationall',
            options={'verbose_name': 'Association All', 'ordering': ['sort'], 'verbose_name_plural': 'Associations All'},
        ),
    ]
