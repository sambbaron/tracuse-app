# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchword', '0006_basemixin_ordering_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watchwordassociationtype',
            options={'ordering': ['sort', '__str__'], 'verbose_name': 'Association Type Watchword'},
        ),
        migrations.AlterModelOptions(
            name='watchworddatumobject',
            options={'ordering': ['sort', '__str__'], 'verbose_name': 'Datum Object Watchword'},
        ),
        migrations.AlterModelOptions(
            name='watchworddatumtype',
            options={'ordering': ['sort', '__str__'], 'verbose_name': 'Datum Type Watchword'},
        ),
    ]
