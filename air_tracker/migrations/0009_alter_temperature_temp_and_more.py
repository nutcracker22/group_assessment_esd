# Generated by Django 4.0.3 on 2022-03-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_tracker', '0008_remove_station_data_pm1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='temp',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='wind_direction',
            name='direction',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='wind_speed',
            name='speed',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True, unique=True),
        ),
    ]
