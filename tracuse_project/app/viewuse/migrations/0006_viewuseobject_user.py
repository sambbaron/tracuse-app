# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viewuse', '0005_entitymodel_names_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewuseobject',
            name='user',
            field=models.ForeignKey(blank=True, related_name='viewuse_objects', null=True, db_column='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
