# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatumGroup',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, max_length=25, blank=True)),
                ('long_definition', models.CharField(null=True, max_length=100, blank=True)),
                ('datum_group_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Datum Group',
                'db_table': 'datum_group',
            },
        ),
        migrations.CreateModel(
            name='DatumObject',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('datum_object_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Datum',
                'db_table': 'datum_object',
            },
        ),
        migrations.CreateModel(
            name='DatumType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, max_length=25, blank=True)),
                ('long_definition', models.CharField(null=True, max_length=100, blank=True)),
                ('datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('repr_expression', models.CharField(max_length=255)),
                ('datum_group', models.ForeignKey(db_column='datum_group_id', to='datum.DatumGroup')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Datum Type',
                'db_table': 'datum_type',
            },
        ),
        migrations.AddField(
            model_name='datumobject',
            name='datum_type',
            field=models.ForeignKey(db_column='datum_type_id', related_name='datum_objects', to='datum.DatumType'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='parent_associations_adjacent',
            field=models.ManyToManyField(to='datum.DatumObject', related_name='child_associations_adjacent', through='association.AssociationAdjacent'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='parent_associations_all',
            field=models.ManyToManyField(to='datum.DatumObject', related_name='child_associations_all', through='association.AssociationAll'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='user',
            field=models.ForeignKey(db_column='user_id', related_name='datum_objects', to=settings.AUTH_USER_MODEL),
        ),
    ]
