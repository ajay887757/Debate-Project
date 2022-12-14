# Generated by Django 3.2.8 on 2022-10-19 08:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('debateApp', '0004_auto_20221019_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debatelist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 16, 41, 86043)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 16, 41, 85274)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 16, 41, 85648)),
        ),
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 16, 41, 87197))),
                ('is_deleted', models.BooleanField(default=False)),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='debateApp.debatelist')),
                ('user1', models.ManyToManyField(to='debateApp.UserProfile')),
            ],
        ),
    ]
