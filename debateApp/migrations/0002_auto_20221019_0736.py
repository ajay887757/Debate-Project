# Generated by Django 3.2.8 on 2022-10-19 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debateApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 7, 36, 55, 114520)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 7, 36, 55, 114954)),
        ),
    ]