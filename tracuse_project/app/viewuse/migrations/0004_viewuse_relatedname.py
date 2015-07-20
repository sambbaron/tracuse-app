# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0003_viewusenested_m2m_fieldnames'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewuseobject',
            name='user',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, db_column='user_id'),
        ),
        migrations.AlterField(
            model_name='viewuseobject',
            name='viewuse_arrangement',
            field=models.ForeignKey(to='viewuse.ViewuseArrangement', db_column='viewuse_arrangement_id'),
        ),
        migrations.AlterField(
            model_name='viewuseobject',
            name='viewuse_datum',
            field=models.ForeignKey(to='viewuse.ViewuseDatum', db_column='viewuse_datum_id'),
        ),
    ]
