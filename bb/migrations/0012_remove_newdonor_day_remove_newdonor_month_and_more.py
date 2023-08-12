# Generated by Django 4.2.2 on 2023-07-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0011_rename_countdown_newdonor_day_newdonor_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newdonor',
            name='day',
        ),
        migrations.RemoveField(
            model_name='newdonor',
            name='month',
        ),
        migrations.AddField(
            model_name='newdonor',
            name='marital',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='newdonor',
            name='nationality',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='newdonor',
            name='question',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='newdonor',
            name='state_of_origin',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
