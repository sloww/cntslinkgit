# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_printer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='is_promotion',
            field=models.BooleanField(default=False),
        ),
    ]
