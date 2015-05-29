# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_label', '0002_auto_20150516_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='description',
            field=models.TextField(),
        ),
    ]
