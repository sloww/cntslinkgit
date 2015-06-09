# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_printer', '0006_auto_20150531_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='resolution',
            field=models.CharField(choices=[('200', '200 dpi'), ('300', '300 dpi'), ('400', '400 dpi'), ('600', '600 dpi')], max_length=3, default='200'),
        ),
    ]
