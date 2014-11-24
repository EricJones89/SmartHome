# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0002_auto_20141110_0327'),
        ('xbee_module', '0002_xbee_module_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xbee_module',
            name='id',
        ),
        migrations.RemoveField(
            model_name='xbee_module',
            name='name',
        ),
        migrations.RemoveField(
            model_name='xbee_module',
            name='url',
        ),
        migrations.AddField(
            model_name='xbee_module',
            name='serialconnections_ptr',
            field=models.OneToOneField(parent_link=True, primary_key=True, auto_created=True, to='Server.SerialConnections', serialize=False, default=True),
            preserve_default=False,
        ),
    ]
