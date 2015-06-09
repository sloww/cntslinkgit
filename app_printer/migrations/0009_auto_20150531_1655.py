# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_printer', '0008_auto_20150531_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='CBase',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('order_index', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=300)),
                ('meta_description', models.TextField(blank=True)),
                ('page_url', models.CharField(max_length=300)),
                ('img_url', models.CharField(blank=True, max_length=300)),
                ('description', django_markdown.models.MarkdownField()),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='description',
        ),
        migrations.RemoveField(
            model_name='article',
            name='id',
        ),
        migrations.RemoveField(
            model_name='article',
            name='name',
        ),
        migrations.RemoveField(
            model_name='article',
            name='set_url',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='description',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='id',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='logo_url',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='name',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='order_index',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='set_url',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='img_url',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='set_url',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='title',
        ),
        migrations.RemoveField(
            model_name='printtype',
            name='description',
        ),
        migrations.RemoveField(
            model_name='printtype',
            name='id',
        ),
        migrations.RemoveField(
            model_name='printtype',
            name='name',
        ),
        migrations.RemoveField(
            model_name='printtype',
            name='order_index',
        ),
        migrations.RemoveField(
            model_name='printtype',
            name='set_url',
        ),
        migrations.AddField(
            model_name='article',
            name='cbase_ptr',
            field=models.OneToOneField(default=1, auto_created=True, serialize=False, primary_key=True, parent_link=True, to='app_printer.CBase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='cbase_ptr',
            field=models.OneToOneField(default=1, auto_created=True, serialize=False, primary_key=True, parent_link=True, to='app_printer.CBase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='printer',
            name='cbase_ptr',
            field=models.OneToOneField(default=1, auto_created=True, serialize=False, primary_key=True, parent_link=True, to='app_printer.CBase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='printtype',
            name='cbase_ptr',
            field=models.OneToOneField(default=1, auto_created=True, serialize=False, primary_key=True, parent_link=True, to='app_printer.CBase'),
            preserve_default=False,
        ),
    ]
