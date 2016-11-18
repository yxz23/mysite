# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('body', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('timestamp', models.DateTimeField(verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3')),
            ],
            options={
                'db_table': 'blog_post',
                'verbose_name': '\u535a\u5ba2',
                'verbose_name_plural': '\u535a\u5ba2s',
            },
        ),
    ]
