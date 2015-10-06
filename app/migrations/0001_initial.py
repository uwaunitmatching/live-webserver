# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_key', models.IntegerField()),
                ('keyword', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uni_id', models.IntegerField()),
                ('unit_code', models.CharField(max_length=20, null=True)),
                ('unit_name', models.CharField(max_length=300, null=True)),
                ('unit_desc', models.CharField(max_length=5000, null=True)),
                ('unit_text', models.CharField(max_length=400, null=True)),
                ('ISBN', models.IntegerField(null=True)),
                ('FreeTags', models.CharField(max_length=5000, null=True)),
                ('Positive', models.CharField(max_length=5000, null=True)),
                ('unit_link', models.URLField(max_length=2084, null=True)),
                ('keywords', models.CharField(max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uni_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=25, null=True)),
                ('country', models.CharField(max_length=25, null=True)),
                ('region', models.CharField(max_length=25, null=True)),
                ('times_ranking', models.CharField(max_length=12, null=True)),
                ('uni_link', models.URLField(max_length=2084)),
            ],
        ),
    ]
