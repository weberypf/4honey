# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=0)),
                ('file_path', models.CharField(max_length=4000)),
                ('log_time', models.BigIntegerField(default=0)),
                ('bear', models.FloatField(default=0)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('gps_speed', models.FloatField(default=0)),
                ('gps_time', models.BigIntegerField(default=0)),
                ('gps_alt', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
