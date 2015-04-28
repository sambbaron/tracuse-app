# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0003_datum_object_associations'),
        ('association', '0003_association_datum_keyword_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssociationTypeDatumType',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('association_type_datum_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('keyword', models.CharField(max_length=100)),
                ('child_datum_type', models.ForeignKey(db_column='child_datum_type_id', related_name='+', to='datum.DatumType')),
                ('parent_datum_type', models.ForeignKey(db_column='parent_datum_type_id', related_name='+', to='datum.DatumType')),
            ],
            options={
                'db_table': 'association_type_datum_type',
                'abstract': False,
            },
        ),
        migrations.AlterIndexTogether(
            name='associationtypedatumtype',
            index_together=set([('parent_datum_type', 'child_datum_type')]),
        ),
    ]
