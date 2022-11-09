# Generated by Django 3.2.8 on 2022-11-09 07:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('debateApp', '0016_auto_20221109_0746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AlterField(
            model_name='debate',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 47, 18, 503738)),
        ),
        migrations.AlterField(
            model_name='debatelist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 47, 18, 503369, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 47, 18, 501268)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 47, 18, 501715)),
        ),
    ]