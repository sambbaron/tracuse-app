# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0010_elementoperator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementoperator',
            options={'verbose_name': 'Element Data Type Operator'},
        ),
    ]
