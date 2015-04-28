# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0003_datum_object_associations'),
        ('filter', '0001_initial'),
        ('association', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssociationDatumKeyword',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('association_keyword_id', models.AutoField(primary_key=True, serialize=False)),
                ('keyword', models.CharField(max_length=100)),
                ('datum_object', models.ForeignKey(related_name='association_keywords', db_column='datum_object_id', to='datum.DatumObject')),
                ('filter_test_scope', models.ForeignKey(null=True, db_column='filter_set_id', related_name='association_keywords', to='filter.FilterSet', blank=True)),
            ],
            options={
                'db_table': 'association_datum_keyword',
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='associationkeyword',
            name='datum_object',
        ),
        migrations.DeleteModel(
            name='AssociationKeyword',
        ),
    ]
