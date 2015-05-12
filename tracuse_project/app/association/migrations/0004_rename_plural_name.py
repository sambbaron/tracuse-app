# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0003_entity_mixin_naming'),
    ]

    operations = [
        migrations.RenameField(
            model_name='associationdirection',
            old_name='plural_name',
            new_name='readable_plural_name',
        ),
        migrations.RenameField(
            model_name='associationtype',
            old_name='plural_name',
            new_name='readable_plural_name',
        ),
    ]
