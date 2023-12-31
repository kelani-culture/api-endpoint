# Generated by Django 3.2.20 on 2023-09-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0005_alter_userinfo_utc_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='current_day',
            field=models.CharField(default='Friday', max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='github_file_url',
            field=models.URLField(default='https://github.com/kelani-culture/api-endpoint/blob/main/my_api/settings.py'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='github_repo_url',
            field=models.URLField(default='https://github.com/kelani-culture/api-endpoint'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='utc_time',
            field=models.CharField(default='2023-09-08T07:51:00Z', max_length=100),
        ),
    ]
