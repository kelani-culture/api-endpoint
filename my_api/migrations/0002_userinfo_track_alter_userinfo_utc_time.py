# Generated by Django 4.1.11 on 2023-09-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='track',
            field=models.CharField(default='backend', max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='utc_time',
            field=models.DateField(default='2023-09-07T13:47:26Z'),
        ),
    ]
