# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=10, verbose_name='\u671f\u6b21')),
            ],
            options={
                'verbose_name': '\u671f\u6b21\u4fe1\u606f',
                'verbose_name_plural': '\u671f\u6b21\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='StudyTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studyTeam', models.CharField(max_length=30, verbose_name='\u7ec4\u540d')),
            ],
            options={
                'verbose_name': '\u5b66\u4e60\u5c0f\u7ec4',
                'verbose_name_plural': '\u5b66\u4e60\u5c0f\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d\uff08\u62fc\u97f3\uff09')),
                ('nameZh', models.CharField(max_length=10, verbose_name='\u59d3\u540d')),
                ('examinationCode', models.CharField(max_length=6, verbose_name='\u5ba1\u67e5\u4ee3\u7801')),
                ('grade', models.ForeignKey(to='examiner_auth.Grade')),
                ('studyTeam', models.ForeignKey(to='examiner_auth.StudyTeam')),
                ('user', models.OneToOneField(related_name='user', null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='\u5ba1\u67e5\u5458\u914d\u7f6e')),
            ],
            options={
                'verbose_name': '\u5ba1\u67e5\u5458\u914d\u7f6e',
                'verbose_name_plural': '\u5ba1\u67e5\u5458\u914d\u7f6e',
            },
        ),
    ]
