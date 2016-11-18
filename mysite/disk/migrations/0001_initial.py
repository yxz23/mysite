# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('headImg', models.FileField(upload_to=b'./upload/')),
            ],
            options={
                'db_table': 'user_img',
                'verbose_name': '\u7528\u6237\u5934\u50cf',
                'verbose_name_plural': '\u7528\u6237\u5934\u50cf',
            },
        ),
    ]
