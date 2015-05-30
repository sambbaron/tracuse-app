# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewuseDatum',
            fields=[
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sort', models.BigIntegerField(default=0, db_index=True)),
                ('entity_name', models.CharField(default='', db_index=True, max_length=40)),
                ('schema_name', models.CharField(default='', max_length=40)),
                ('readable_name', models.CharField(default='', db_index=True, max_length=40)),
                ('readable_plural_name', models.CharField(default='', max_length=40)),
                ('short_definition', models.CharField(blank=True, null=True, max_length=25)),
                ('long_definition', models.CharField(blank=True, null=True, max_length=100)),
                ('example', models.CharField(blank=True, null=True, max_length=100)),
                ('viewuse_datum_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'viewuse_datum',
                'abstract': False,
                'verbose_name': 'Viewuse Datum Template',
            },
        ),
        migrations.AlterModelOptions(
            name='viewusearrangement',
            options={'verbose_name': 'Viewuse Arrangement Template'},
        ),
        migrations.RemoveField(
            model_name='viewusearrangement',
            name='template_path',
        ),
        migrations.AddField(
            model_name='viewuseobject',
            name='viewuse_datum',
            field=models.ForeignKey(default=0, to='viewuse.ViewuseDatum', db_column='viewuse_datum_id', related_name='viewuse_objects'),
            preserve_default=False,
        ),
    ]
