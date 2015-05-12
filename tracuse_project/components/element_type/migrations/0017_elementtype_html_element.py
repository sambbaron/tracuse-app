# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0016_null_string_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementtype',
            name='html_element',
            field=models.CharField(max_length=25, default='text'),
        ),
    ]
