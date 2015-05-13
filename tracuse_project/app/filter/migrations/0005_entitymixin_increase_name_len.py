# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0004_remove_field_usage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterset',
            name='entity_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='filterset',
            name='readable_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='filterset',
            name='readable_plural_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='filterset',
            name='schema_name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
