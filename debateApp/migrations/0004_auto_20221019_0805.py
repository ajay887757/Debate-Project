# Generated by Django 3.2.8 on 2022-10-19 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debateApp', '0003_auto_20221019_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='debatelist',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='role',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='debatelist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 5, 45, 848627)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 5, 45, 847394)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 5, 45, 848025)),
        ),
    ]
