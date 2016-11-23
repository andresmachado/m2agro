# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductServiceRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='service',
        ),
        migrations.AddField(
            model_name='productservicerelationship',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product', verbose_name='Produto'),
        ),
        migrations.AddField(
            model_name='productservicerelationship',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Service', verbose_name='Serviço'),
        ),
        migrations.AddField(
            model_name='service',
            name='product',
            field=models.ManyToManyField(related_name='products', through='api.ProductServiceRelationship', to='api.Product', verbose_name='Serviço'),
        ),
    ]