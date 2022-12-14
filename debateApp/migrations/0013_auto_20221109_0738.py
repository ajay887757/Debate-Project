# Generated by Django 3.2.8 on 2022-11-09 07:38

import datetime
import debateApp.models
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('debateApp', '0012_auto_20221109_0730'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('objects', debateApp.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='debate',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 38, 0, 778525)),
        ),
        migrations.AlterField(
            model_name='debatelist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 38, 0, 778149, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 38, 0, 776145)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 7, 38, 0, 776529)),
        ),
    ]
