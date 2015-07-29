# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filterruledatatype',
            old_name='elvalue',
            new_name='element_value',
        ),
        migrations.RenameField(
            model_name='filterruleelement',
            old_name='elvalue',
            new_name='element_value',
        ),
    ]
