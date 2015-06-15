# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element_type', '0012_entitymodel_names_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementdatumtype',
            name='primary_view',
            field=models.BooleanField(default=False),
        ),
    ]
