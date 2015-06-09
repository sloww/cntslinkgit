# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, editable=False),
        ),
    ]
