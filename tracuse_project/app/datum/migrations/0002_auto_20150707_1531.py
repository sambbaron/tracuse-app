# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('association', '0002_auto_20150707_1531'),
        ('datum', '0001_initial'),
        ('element_type', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datumtype',
            name='element_types',
            field=models.ManyToManyField(related_name='+', to='element_type.ElementType', through='element_type.ElementDatumType'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='adjacent_child_datums',
            field=models.ManyToManyField(related_name='adjacent_parent_datums', to='datum.DatumObject', through='association.AssociationAdjacent'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='all_child_datums',
            field=models.ManyToManyField(related_name='all_parent_datums', to='datum.DatumObject', through='association.AssociationAll'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='datum_type',
            field=models.ForeignKey(related_name='datum_objects', db_column='datum_type_id', to='datum.DatumType'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='element_types',
            field=models.ManyToManyField(related_name='+', to='element_type.ElementType', through='element_type.ElementDatumObject'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='user',
            field=models.ForeignKey(related_name='datum_objects', db_column='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
