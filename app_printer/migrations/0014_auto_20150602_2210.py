# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_page', '0001_initial'),
        ('app_printer', '0013_auto_20150602_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cbase',
            name='page_ptr',
        ),
        migrations.AddField(
            model_name='cbase',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='ID', default=0, auto_created=True, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cbase',
            name='page',
            field=models.ForeignKey(default=0, to='app_page.Page'),
            preserve_default=False,
        ),
    ]
