# Generated by Django 4.2.2 on 2023-07-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockIncrease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(blank=True, max_length=50)),
                ('unit', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
