# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='bear',
            new_name='altitude',
        ),
        migrations.RemoveField(
            model_name='message',
            name='gps_alt',
        ),
        migrations.RemoveField(
            model_name='message',
            name='gps_speed',
        ),
        migrations.RemoveField(
            model_name='message',
            name='gps_time',
        ),
        migrations.AddField(
            model_name='message',
            name='address',
            field=models.CharField(default=b'', max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
