# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0003_repr_expression_to_str_expression'),
    ]

    operations = [
        migrations.AddField(
            model_name='datumgroup',
            name='usage',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datumtype',
            name='usage',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
