# Generated by Django 3.2.8 on 2022-10-19 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debateApp', '0005_auto_20221019_0816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debate',
            old_name='user1',
            new_name='users',
        ),
        migrations.AlterField(
            model_name='debate',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 33, 8, 760824)),
        ),
        migrations.AlterField(
            model_name='debatelist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 33, 8, 759046)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 33, 8, 758049)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 33, 8, 758558)),
        ),
    ]
