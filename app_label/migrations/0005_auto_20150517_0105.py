# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_label', '0004_auto_20150517_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='description',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
