from django.db import models

# Create your models here.

class station_details(models.Model):
    site_name = models.CharField(max_length=200)
    site_type = models.CharField(max_length=200)
    latitude = models.DecimalField
    longitue = models.DecimalField
    site_comments = models.TextField

    def __str__(self):
        return f'{self.site_name},{self.site_type},{self.latitude},{self.longitue}'


class dates(models.Model):
    date = models.DateField


class times(models.Model):
    time = models.TimeField


class wind_direction(models.Model):
    direction = models.IntegerField


class wind_speed(models.Model):
    speed = models.DecimalField


class temperature(models.Model):
    temp = models.DecimalField


class station_data(models.Model):
    date = models.ForeignKey(dates)
    time = models.ForeignKey(times)
    wind_direction = models.ForeignKey(wind_direction)
    wind_speed = models.ForeignKey(wind_speed)
    temperature = models.ForeignKey(temperature)
    nitric_oxide = models.DecimalField
    nitrogen_dioxide = models.DecimalField
    nitrogen_oxides = models.DecimalField
    pm10 = models.DecimalField
    pm2point5 = models.DecimalField
    pm1 = models.DecimalField
    ozone = models.DecimalField
    station_details ???