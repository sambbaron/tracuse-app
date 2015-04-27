# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datumobject',
            name='datum_type',
            field=models.ForeignKey(to='datum.DatumType', db_column='datum_type_id', related_name='datum_objects'),
        ),
        migrations.AlterField(
            model_name='datumobject',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column='user_id', related_name='datum_objects'),
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='datum_group',
            field=models.ForeignKey(to='datum.DatumGroup', db_column='datum_group_id', related_name='datum_types'),
        ),
    ]
