# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_printer', '0009_auto_20150531_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrinterType',
            fields=[
                ('cbase_ptr', models.OneToOneField(serialize=False, to='app_printer.CBase', parent_link=True, primary_key=True, auto_created=True)),
                ('count_daily', models.CharField(max_length=300, default='4000')),
            ],
            options={
                'verbose_name_plural': 'Type Set',
            },
            bases=('app_printer.cbase',),
        ),
        migrations.RemoveField(
            model_name='printtype',
            name='cbase_ptr',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='print_type',
        ),
        migrations.DeleteModel(
            name='PrintType',
        ),
        migrations.AddField(
            model_name='printer',
            name='printer_type',
            field=models.ForeignKey(default=1, to='app_printer.PrinterType'),
            preserve_default=False,
        ),
    ]
