# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161122_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='product',
            field=models.ManyToManyField(related_name='services', through='api.ProductServiceRelationship', to='api.Product', verbose_name='Serviço'),
        ),
    ]
