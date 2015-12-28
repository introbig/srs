# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('question', models.TextField(blank=True, null=True, default='')),
                ('answer', models.TextField(blank=True, null=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('current_rank', models.CharField(max_length=200, blank=True, null=True)),
                ('last_seen', models.DateTimeField(blank=True, null=True)),
                ('image', models.CharField(max_length=200, blank=True, null=True)),
                ('recording', models.CharField(max_length=200, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200, blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(to='cards.Deck'),
        ),
    ]
