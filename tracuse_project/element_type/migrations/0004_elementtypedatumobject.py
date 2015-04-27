# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0003_datum_object_associations'),
        ('element_type', '0003_foreign_key_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementTypeDatumObject',
            fields=[
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('element_type_datum_object_id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_object', models.ForeignKey(to='datum.DatumObject', related_name='element_types', db_column='datum_object_id')),
                ('element_type', models.ForeignKey(to='element_type.ElementType', related_name='datum_objects', db_column='element_type_id')),
            ],
            options={
                'abstract': False,
                'db_table': 'element_type_datum_object',
            },
        ),
        migrations.AlterUniqueTogether(
            name='elementtypedatumobject',
            unique_together=set([('datum_object', 'element_type')]),
        ),
        migrations.AlterIndexTogether(
            name='elementtypedatumobject',
            index_together=set([('datum_object', 'element_type')]),
        ),
    ]
