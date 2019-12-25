# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-12-21 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191221_1412'),
        ('teacher', '0002_auto_20191221_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, verbose_name='考试分数')),
            ],
        ),
        migrations.RemoveField(
            model_name='exam',
            name='course',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='user',
        ),
        migrations.AddField(
            model_name='course',
            name='course_desc',
            field=models.TextField(default='', verbose_name='课程描述'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='user',
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(to='user.User'),
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.AddField(
            model_name='score',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.Course'),
        ),
        migrations.AddField(
            model_name='score',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
