# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('description_short', models.TextField(verbose_name='краткое описание')),
                ('description_full', models.TextField(verbose_name='полное описание')),
                ('date_start', models.DateField(verbose_name='дата начала')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='дата окончания')),
                ('time_start', models.TimeField(blank=True, null=True, verbose_name='время начала')),
                ('time_end', models.TimeField(blank=True, null=True, verbose_name='время окончания')),
                ('location', models.CharField(blank=True, max_length=100, verbose_name='место проведения')),
                ('cost', models.CharField(blank=True, max_length=50, verbose_name='стоимость')),
                ('url', models.URLField(verbose_name='ссылка')),
            ],
            options={
                'verbose_name': 'событие',
                'verbose_name_plural': 'события',
                'ordering': ('date_start',),
            },
        ),
    ]
