# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Height',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('height', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('setUrl', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=2000)),
                ('description', models.CharField(max_length=1000)),
                ('height', models.ForeignKey(to='app_label.Height')),
            ],
            options={
                'verbose_name': 'Label',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('imgUrl', models.CharField(max_length=100)),
                ('setUrl', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Width',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('width', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='label',
            name='material',
            field=models.ForeignKey(to='app_label.Material'),
        ),
        migrations.AddField(
            model_name='label',
            name='width',
            field=models.ForeignKey(to='app_label.Width'),
        ),
        migrations.AlterUniqueTogether(
            name='label',
            unique_together=set([('material', 'width', 'height', 'id')]),
        ),
    ]
