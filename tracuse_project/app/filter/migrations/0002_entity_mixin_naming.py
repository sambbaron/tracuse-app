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
            name='plural_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='filterset',
            name='readable_name',
            field=models.CharField(default='', max_length=25, db_index=True),
        ),
        migrations.AddField(
            model_name='filterset',
            name='schema_name',
            field=models.CharField(default='', max_length=25),
        ),
    ]
