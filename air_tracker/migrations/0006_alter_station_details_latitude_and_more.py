# Generated by Django 4.0.3 on 2022-03-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_tracker', '0005_alter_dates_date_alter_times_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station_details',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='station_details',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
