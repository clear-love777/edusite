# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-12-21 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191221_1412'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='考试分数')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_student_amount',
            field=models.IntegerField(default=50, verbose_name='最多可选学生数'),
        ),
        migrations.AddField(
            model_name='exam',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.Course'),
        ),
        migrations.AddField(
            model_name='exam',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
