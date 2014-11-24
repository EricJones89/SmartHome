# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='xbee_module',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('destinationAddress', models.TextField(max_length=16)),
                ('networkAddress', models.TextField(max_length=4)),
                ('serialNumber', models.TextField(max_length=16)),
                ('pan_id', models.TextField(max_length=16)),
                ('name', models.TextField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
