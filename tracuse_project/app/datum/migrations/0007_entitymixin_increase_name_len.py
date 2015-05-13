# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0006_remove_field_usage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datumgroup',
            name='entity_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='datumgroup',
            name='readable_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='datumgroup',
            name='readable_plural_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='datumgroup',
            name='schema_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='entity_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='readable_name',
            field=models.CharField(db_index=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='readable_plural_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='schema_name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
