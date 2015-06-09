# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_printer', '0007_auto_20150531_1550'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Resolution',
        ),
        migrations.AlterField(
            model_name='printer',
            name='max_width',
            field=models.CharField(max_length=3, choices=[('0', '4 英寸'), ('1', '6 英寸'), ('2', '2 英寸'), ('3', '其他')], default='0'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='ribbon_size',
            field=models.CharField(max_length=3, choices=[('0', '大卷芯 (25.4 mm)'), ('1', '小卷芯 (12.7 mm)'), ('3', '其他')], default='0'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='ribbon_type',
            field=models.CharField(max_length=3, choices=[('0', '外碳'), ('1', '内碳'), ('2', '外碳和内碳'), ('3', '无')], default='0'),
        ),
        migrations.DeleteModel(
            name='MaxWidth',
        ),
        migrations.DeleteModel(
            name='RibbonSize',
        ),
        migrations.DeleteModel(
            name='RibbonType',
        ),
    ]
