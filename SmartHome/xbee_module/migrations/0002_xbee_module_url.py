# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xbee_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xbee_module',
            name='url',
            field=models.TextField(default='url', max_length=256),
            preserve_default=True,
        ),
    ]
