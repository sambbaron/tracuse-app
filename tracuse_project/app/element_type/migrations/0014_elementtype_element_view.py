# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0013_elementdatumtype_primary_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementtype',
            name='html_element',
        ),
        migrations.AddField(
            model_name='elementtype',
            name='element_view',
            field=models.CharField(max_length=25, default='ElementText'),
        ),
    ]
