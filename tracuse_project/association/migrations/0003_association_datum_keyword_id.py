# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0002_association_datum_keyword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='associationdatumkeyword',
            old_name='association_keyword_id',
            new_name='association_datum_keyword_id',
        ),
    ]
