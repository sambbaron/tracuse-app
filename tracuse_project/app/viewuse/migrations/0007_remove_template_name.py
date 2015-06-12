# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0006_viewuseobject_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viewusearrangement',
            options={'verbose_name': 'Viewuse Arrangement'},
        ),
        migrations.AlterModelOptions(
            name='viewusedatum',
            options={'verbose_name': 'Viewuse Datum'},
        ),
    ]
