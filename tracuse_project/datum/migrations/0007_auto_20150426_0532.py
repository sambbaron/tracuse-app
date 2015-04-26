# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datum', '0006_auto_20150424_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatumObject',
            fields=[
                ('sort', models.IntegerField(db_index=True, default=0, db_default='0')),
                ('active', models.BooleanField(db_default='True', default=True, db_index=True)),
                ('datum_object_id', models.AutoField(serialize=False, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_default='CURRENT_TIMESTAMP')),
            ],
            options={
                'abstract': False,
                'db_table': 'datum_object',
            },
        ),
        migrations.AlterField(
            model_name='datumgroup',
            name='active',
            field=models.BooleanField(db_default='True', default=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='datumgroup',
            name='sort',
            field=models.IntegerField(db_index=True, default=0, db_default='0'),
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='active',
            field=models.BooleanField(db_default='True', default=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='datumtype',
            name='sort',
            field=models.IntegerField(db_index=True, default=0, db_default='0'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='datum_type',
            field=models.ForeignKey(db_column='datum_type_id', to='datum.DatumType'),
        ),
        migrations.AddField(
            model_name='datumobject',
            name='user',
            field=models.ForeignKey(db_column='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
