# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('passwd', models.CharField(max_length=50, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
            ],
            options={
                'db_table': 'account',
                'verbose_name': '\u7528\u6237\u8868',
                'verbose_name_plural': '\u7528\u6237\u8868',
            },
        ),
    ]
