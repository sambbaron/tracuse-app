# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0004_associationtypedatumtype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='associationadjacent',
            options={'verbose_name': 'Association Adjacent', 'verbose_name_plural': 'Associations Adjacent'},
        ),
        migrations.AlterModelOptions(
            name='associationall',
            options={'verbose_name': 'Association All', 'verbose_name_plural': 'Associations All'},
        ),
        migrations.AlterModelOptions(
            name='associationdatumkeyword',
            options={'verbose_name': 'Association Datum Keyword'},
        ),
        migrations.AlterModelOptions(
            name='associationdirection',
            options={'verbose_name': 'Association Direction'},
        ),
        migrations.AlterModelOptions(
            name='associationtype',
            options={'verbose_name': 'Association Type'},
        ),
        migrations.AlterModelOptions(
            name='associationtypedatumtype',
            options={'verbose_name': 'Association Datum Type Map'},
        ),
    ]
