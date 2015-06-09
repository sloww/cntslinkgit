# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_printer', '0002_auto_20150530_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='article',
            field=models.ForeignKey(to='app_printer.Article', default=1),
            preserve_default=False,
        ),
    ]
