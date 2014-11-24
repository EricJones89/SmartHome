# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serialconnections',
            old_name='text',
            new_name='name',
        ),
        migrations.AddField(
            model_name='serialconnections',
            name='location_url',
            field=models.CharField(max_length=100, default='none'),
            preserve_default=False,
        ),
    ]
