# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_label', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='setUrl',
            field=models.CharField(max_length=100, db_index=True),
        ),
    ]
