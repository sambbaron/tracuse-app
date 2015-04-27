# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0002_foreign_key_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssociationAdjacent',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('association_adjacent_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'association_adjacent',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssociationAll',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('association_all_id', models.AutoField(serialize=False, primary_key=True)),
                ('depth', models.IntegerField(default=0)),
                ('child_datum', models.ForeignKey(related_name='+', db_column='child_datum_id', to='datum.DatumObject')),
                ('parent_datum', models.ForeignKey(related_name='+', db_column='parent_datum_id', to='datum.DatumObject')),
            ],
            options={
                'db_table': 'association_all',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssociationDirection',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(max_length=25, default='', db_index=True)),
                ('short_definition', models.CharField(max_length=25, null=True, blank=True)),
                ('long_definition', models.CharField(max_length=100, null=True, blank=True)),
                ('association_direction_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'association_direction',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssociationKeyword',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('association_keyword_id', models.AutoField(serialize=False, primary_key=True)),
                ('keyword', models.CharField(max_length=100)),
                ('datum_object', models.ForeignKey(related_name='association_keywords', db_column='datum_object_id', to='datum.DatumObject')),
            ],
            options={
                'db_table': 'association_keyword',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssociationType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('entity_name', models.CharField(max_length=25, default='', db_index=True)),
                ('short_definition', models.CharField(max_length=25, null=True, blank=True)),
                ('long_definition', models.CharField(max_length=100, null=True, blank=True)),
                ('association_type_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'association_type',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='associationadjacent',
            name='association_type',
            field=models.ForeignKey(related_name='associations_adjacent', db_column='association_type_id', to='association.AssociationType'),
        ),
        migrations.AddField(
            model_name='associationadjacent',
            name='child_datum',
            field=models.ForeignKey(related_name='+', db_column='child_datum_id', to='datum.DatumObject'),
        ),
        migrations.AddField(
            model_name='associationadjacent',
            name='parent_datum',
            field=models.ForeignKey(related_name='+', db_column='parent_datum_id', to='datum.DatumObject'),
        ),
        migrations.AlterUniqueTogether(
            name='associationall',
            unique_together=set([('parent_datum', 'child_datum')]),
        ),
        migrations.AlterIndexTogether(
            name='associationall',
            index_together=set([('parent_datum', 'child_datum')]),
        ),
        migrations.AlterUniqueTogether(
            name='associationadjacent',
            unique_together=set([('parent_datum', 'child_datum')]),
        ),
        migrations.AlterIndexTogether(
            name='associationadjacent',
            index_together=set([('parent_datum', 'child_datum')]),
        ),
    ]
