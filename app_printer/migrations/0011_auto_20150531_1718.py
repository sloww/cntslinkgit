# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_printer', '0010_auto_20150531_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='Printer_height',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='Printer_length',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='Printer_width',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='article',
            field=models.ManyToManyField(to='app_printer.Article', blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='catalogue_url',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='diver_url',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='img_banner',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='max_speed',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='memory_size',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
