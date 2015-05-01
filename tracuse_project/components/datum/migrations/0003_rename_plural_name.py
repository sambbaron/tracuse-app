# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0002_entity_mixin_naming'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datumgroup',
            old_name='plural_name',
            new_name='readable_plural_name',
        ),
        migrations.RenameField(
            model_name='datumtype',
            old_name='plural_name',
            new_name='readable_plural_name',
        ),
    ]
