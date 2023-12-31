# Generated by Django 4.1.11 on 2023-09-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_name', models.CharField(max_length=50)),
                ('current_day', models.CharField(default='Thursday', max_length=10)),
                ('utc_time', models.DateField(default='2023-09-07T13:40:33Z')),
                ('github_file_url', models.URLField()),
                ('github_repo_url', models.URLField()),
                ('status_code', models.IntegerField(default=200)),
            ],
        ),
    ]
