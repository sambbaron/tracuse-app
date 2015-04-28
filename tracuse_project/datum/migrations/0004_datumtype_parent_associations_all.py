# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0004_associationtypedatumtype'),
        ('datum', '0003_datum_object_associations'),
    ]

    operations = [
        migrations.AddField(
            model_name='datumtype',
            name='parent_associations_all',
            field=models.ManyToManyField(to='datum.DatumType', through='association.AssociationAll', related_name='child_associations_all'),
        ),
    ]
