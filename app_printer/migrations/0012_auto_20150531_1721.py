# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_printer', '0011_auto_20150531_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbase',
            name='description',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
        migrations.AlterField(
            model_name='cbase',
            name='page_url',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
