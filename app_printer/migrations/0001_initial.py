# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('description', django_markdown.models.MarkdownField()),
                ('set_url', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Article Related ',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('order_index', models.IntegerField(default=0)),
                ('set_url', models.CharField(max_length=300)),
                ('nation', models.CharField(max_length=300)),
                ('logo_url', models.CharField(max_length=300)),
                ('diver_url', models.CharField(max_length=300)),
                ('description', django_markdown.models.MarkdownField()),
            ],
            options={
                'verbose_name_plural': 'Brand Set',
            },
        ),
        migrations.CreateModel(
            name='MaxWidth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_width', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Max Width Set ',
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('set_url', models.CharField(max_length=300)),
                ('is_thermal_only', models.BooleanField(default=False)),
                ('max_speed', models.CharField(max_length=300)),
                ('memory_size', models.CharField(max_length=300)),
                ('weight', models.IntegerField(default=0)),
                ('Printer_length', models.IntegerField(default=0)),
                ('Printer_width', models.IntegerField(default=0)),
                ('Printer_height', models.IntegerField(default=0)),
                ('catalogue_url', models.CharField(max_length=300)),
                ('diver_url', models.CharField(max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('description', django_markdown.models.MarkdownField()),
                ('img_url', models.CharField(max_length=300)),
                ('img_banner', models.CharField(max_length=300)),
                ('show_style', models.IntegerField(default=0)),
                ('is_public', models.BooleanField(default=False)),
                ('is_promotion', models.IntegerField(default=False)),
                ('brand', models.ForeignKey(to='app_printer.Brand')),
                ('max_width', models.ForeignKey(to='app_printer.MaxWidth')),
            ],
            options={
                'verbose_name_plural': 'Printer Set ',
            },
        ),
        migrations.CreateModel(
            name='PrintType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('order_index', models.IntegerField(default=0)),
                ('set_url', models.CharField(max_length=300)),
                ('count_daily', models.CharField(max_length=300)),
                ('description', django_markdown.models.MarkdownField()),
            ],
            options={
                'verbose_name_plural': 'Type Set',
            },
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resolution', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Resolution Set ',
            },
        ),
        migrations.CreateModel(
            name='RibbonSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ribbon_size', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Ribbon Size Set ',
            },
        ),
        migrations.CreateModel(
            name='RibbonType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ribbon_type', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Ribbon Type Set ',
            },
        ),
        migrations.AddField(
            model_name='printer',
            name='print_type',
            field=models.ForeignKey(to='app_printer.PrintType'),
        ),
        migrations.AddField(
            model_name='printer',
            name='resolution',
            field=models.ForeignKey(to='app_printer.Resolution'),
        ),
        migrations.AddField(
            model_name='printer',
            name='ribbon_size',
            field=models.ForeignKey(to='app_printer.RibbonSize'),
        ),
        migrations.AddField(
            model_name='printer',
            name='ribbon_type',
            field=models.ForeignKey(to='app_printer.RibbonType'),
        ),
    ]
