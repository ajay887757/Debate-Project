# Generated by Django 3.2.8 on 2022-10-28 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debateApp', '0008_auto_20221028_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debate',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 7, 49, 6, 929481)),
        ),
        migrations.AlterField(
            model_name='debatelist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 7, 49, 6, 928193)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 7, 49, 6, 927143)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 7, 49, 6, 927735)),
        ),
    ]
