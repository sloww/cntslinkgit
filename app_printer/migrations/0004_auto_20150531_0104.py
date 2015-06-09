# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_printer', '0003_printer_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maxwidth',
            options={'verbose_name_plural': 'Max Width'},
        ),
        migrations.AlterModelOptions(
            name='printer',
            options={'verbose_name_plural': 'Printers'},
        ),
        migrations.AlterModelOptions(
            name='resolution',
            options={'verbose_name_plural': 'Resolution'},
        ),
        migrations.AlterModelOptions(
            name='ribbonsize',
            options={'verbose_name_plural': 'Ribbon Size'},
        ),
        migrations.AlterModelOptions(
            name='ribbontype',
            options={'verbose_name_plural': 'Ribbon Type'},
        ),
        migrations.RemoveField(
            model_name='printer',
            name='article',
        ),
        migrations.AddField(
            model_name='printer',
            name='article',
            field=models.ManyToManyField(to='app_printer.Article'),
        ),
    ]
