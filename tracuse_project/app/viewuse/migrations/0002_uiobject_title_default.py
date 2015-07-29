# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewuseobject',
            name='title',
            field=models.CharField(blank=True, default='', null=True, max_length=100),
        ),
    ]
