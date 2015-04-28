# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_value', '0003_element_option_nullable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementvaluebinary',
            options={'verbose_name': 'Element Value'},
        ),
        migrations.AlterModelOptions(
            name='elementvalueboolean',
            options={'verbose_name': 'Element Value'},
        ),
        migrations.AlterModelOptions(
            name='elementvaluedatetime',
            options={'verbose_name': 'Element Value'},
        ),
        migrations.AlterModelOptions(
            name='elementvaluedecimal',
            options={'verbose_name': 'Element Value'},
        ),
        migrations.AlterModelOptions(
            name='elementvaluestring',
            options={'verbose_name': 'Element Value'},
        ),
        migrations.AlterModelOptions(
            name='elementvaluetextdata',
            options={'verbose_name': 'Element Value'},
        ),
    ]
