# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_printer', '0004_auto_20150531_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='resolution',
            field=models.CharField(max_length=3, choices=[('200', '200'), ('300', '300'), ('400', '400'), ('600', '600')]),
        ),
    ]
