# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0005_meta_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='associationdatumkeyword',
            name='datum_object',
        ),
        migrations.RemoveField(
            model_name='associationdatumkeyword',
            name='filter_test_scope',
        ),
        migrations.AlterIndexTogether(
            name='associationtypedatumtype',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='associationtypedatumtype',
            name='child_datum_type',
        ),
        migrations.RemoveField(
            model_name='associationtypedatumtype',
            name='parent_datum_type',
        ),
        migrations.DeleteModel(
            name='AssociationDatumKeyword',
        ),
        migrations.DeleteModel(
            name='AssociationTypeDatumType',
        ),
    ]
