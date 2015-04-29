# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('association', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatumGroup',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('datum_group_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'datum_group',
                'abstract': False,
                'verbose_name': 'Datum Group',
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
                'db_table': 'datum_object',
                'abstract': False,
                'verbose_name': 'Datum',
            },
        ),
        migrations.CreateModel(
            name='DatumType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(default='', max_length=25, db_index=True)),
                ('short_definition', models.CharField(null=True, blank=True, max_length=25)),
                ('long_definition', models.CharField(null=True, blank=True, max_length=100)),
                ('datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('repr_expression', models.CharField(max_length=255)),
                ('datum_group', models.ForeignKey(to='datum.DatumGroup', db_column='datum_group_id')),
                ('parent_associations_all', models.ManyToManyField(through='association.AssociationAll', related_name='child_associations_all', to='datum.DatumType')),
            ],
            options={
                'db_table': 'datum_type',
                'abstract': False,
                'verbose_name': 'Datum Type',
            },
        ),
        migrations.AddField(
            model_name='datumobject',
            name='datum_type',
            field=models.ForeignKey(related_name='datum_objects', db_column='datum_type_id', to='datum.DatumType'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='parent_associations_adjacent',
            field=models.ManyToManyField(through='association.AssociationAdjacent', related_name='child_associations_adjacent', to='datum.DatumObject'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='parent_associations_all',
            field=models.ManyToManyField(through='association.AssociationAll', related_name='child_associations_all', to='datum.DatumObject'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='user',
            field=models.ForeignKey(related_name='datum_objects', db_column='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
