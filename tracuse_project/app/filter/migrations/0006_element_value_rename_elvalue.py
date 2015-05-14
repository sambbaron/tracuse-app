# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('filter', '0005_entitymixin_increase_name_len'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filterruleelement',
            old_name='element_value',
            new_name='elvalue',
        ),
    ]
