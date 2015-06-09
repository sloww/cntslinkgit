# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_printer', '0014_auto_20150602_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbase',
            name='id',
            field=models.UUIDField(primary_key=True, editable=False, serialize=False, default=uuid.uuid4),
        ),
    ]
