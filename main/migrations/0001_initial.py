# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artistId', models.BigIntegerField()),
                ('albumId', models.BigIntegerField()),
                ('artistName', models.CharField(max_length=200)),
                ('albumName', models.CharField(max_length=200)),
                ('artworkUrl100', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
