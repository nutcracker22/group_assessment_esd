from django.db import models

# Create your models here.

class Station_details(models.Model):
    site_name = models.CharField(max_length=200)
    site_type = models.CharField(max_length=200)
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    site_comments = models.TextField()

    def __str__(self):
        return f'{self.site_name},{self.site_type},{self.latitude},{self.longitude}'


class Dates(models.Model):
    date = models.DateField(input_formats=['%d/%m/%Y'])


class Times(models.Model):
    time = models.TimeField()


class Wind_direction(models.Model):
    direction = models.IntegerField()


class Wind_speed(models.Model):
    speed = models.DecimalField()


class Temperature(models.Model):
    temp = models.DecimalField()


class Station_data(models.Model):
    date = models.ForeignKey(Dates)
    time = models.ForeignKey(Times)
    wind_direction = models.ForeignKey(Wind_direction)
    wind_speed = models.ForeignKey(Wind_speed)
    temperature = models.ForeignKey(Temperature)
    nitric_oxide = models.DecimalField()
    nitrogen_dioxide = models.DecimalField()
    nitrogen_oxides = models.DecimalField()
    pm10 = models.DecimalField()
    pm2point5 = models.DecimalField()
    pm1 = models.DecimalField()
    ozone = models.DecimalField()
    Station_details ???