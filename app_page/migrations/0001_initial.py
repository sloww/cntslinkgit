# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('_domain', models.CharField(max_length=300, blank=True)),
                ('_title', models.CharField(max_length=300, blank=True)),
                ('_logo', models.CharField(max_length=300, blank=True)),
                ('_visit_count', models.CharField(max_length=300, blank=True)),
            ],
        ),
    ]
