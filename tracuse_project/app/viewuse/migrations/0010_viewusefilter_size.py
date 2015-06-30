# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0009_revise_viewuseobject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewuseobject',
            name='viewuse_filter',
            field=models.TextField(null=True, blank=True, default=''),
        ),
    ]
