# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_label', '0003_auto_20150516_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='is_show',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='label',
            name='is_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='material',
            name='description',
            field=models.TextField(),
        ),
    ]
