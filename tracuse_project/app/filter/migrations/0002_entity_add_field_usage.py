# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filterset',
            name='usage',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
