# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewuse', '0004_viewuse_relatedname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewuseobject',
            old_name='datum_filter',
            new_name='datum_filter',
        ),
    ]
