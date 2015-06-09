# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_page', '0001_initial'),
        ('app_printer', '0012_auto_20150531_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cbase',
            name='id',
        ),
        migrations.AddField(
            model_name='cbase',
            name='page_ptr',
            field=models.OneToOneField(default=0, auto_created=True, to='app_page.Page', serialize=False, primary_key=True, parent_link=True),
            preserve_default=False,
        ),
    ]
