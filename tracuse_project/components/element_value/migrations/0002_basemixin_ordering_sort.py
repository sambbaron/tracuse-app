# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_value', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementvaluebinary',
            options={'ordering': ['sort'], 'verbose_name': 'Element Value'},
        ),
        migrations.AlterModelOptions(
            name='elementvalueboolean',
            options={'ordering': ['sort'], 'verbose_name': 'Element Value'},
        ),
        migrations.AlterModelOptions(
            name='elementvaluedatetime',
            options={'ordering': ['sort'], 'verbose_name': 'Element Value'},
        ),
        migrations.AlterModelOptions(
            name='elementvaluedecimal',
            options={'ordering': ['sort'], 'verbose_name': 'Element Value'},
        ),
        migrations.AlterModelOptions(
            name='elementvaluestring',
            options={'ordering': ['sort'], 'verbose_name': 'Element Value'},
        ),
        migrations.AlterModelOptions(
            name='elementvaluetextdata',
            options={'ordering': ['sort'], 'verbose_name': 'Element Value'},
        ),
    ]
