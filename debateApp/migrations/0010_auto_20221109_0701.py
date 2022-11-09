# Generated by Django 3.2.8 on 2022-11-09 07:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('debateApp', '0009_auto_20221028_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debate',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 1, 46, 695747)),
        ),
        migrations.AlterField(
            model_name='debatelist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 1, 46, 695372, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 1, 46, 694483)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 1, 46, 694960)),
        ),
        migrations.DeleteModel(
            name='ChildClass',
        ),
    ]