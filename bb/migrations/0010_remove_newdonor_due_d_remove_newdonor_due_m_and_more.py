# Generated by Django 4.2.2 on 2023-07-14 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0009_newdonor_due_d_newdonor_due_m'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newdonor',
            name='due_d',
        ),
        migrations.RemoveField(
            model_name='newdonor',
            name='due_m',
        ),
        migrations.AddField(
            model_name='newdonor',
            name='countdown',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
