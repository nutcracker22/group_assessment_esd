from django.db import models

# Create your models here.

class Station_details(models.Model):
    site_name = models.CharField(max_length=200)
    site_type = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=2, decimal_places=2)
    longitude = models.DecimalField(max_digits=2, decimal_places=2)
    site_comments = models.TextField()

    def __str__(self):
        return f'{self.site_name},{self.site_type},{self.latitude},{self.longitude}'


class Dates(models.Model):
    date = models.DateField(unique=True)


class Times(models.Model):
    time = models.TimeField(unique=True)


class Wind_direction(models.Model):
    direction = models.IntegerField(blank=True, unique=True)


class Wind_speed(models.Model):
    speed = models.DecimalField(max_digits=3, decimal_places=1, blank=True, unique=True)


class Temperature(models.Model):
    temp = models.DecimalField(max_digits=3, decimal_places=1, blank=True, unique=True)

"""
class Station_data(models.Model):
    date = models.ForeignKey('Dates', on_delete=models.CASCADE)
    time = models.ForeignKey('Times', on_delete=models.CASCADE)
    wind_direction = models.ForeignKey('Wind_direction', on_delete=models.CASCADE)
    wind_speed = models.ForeignKey('Wind_speed', on_delete=models.CASCADE)
    temperature = models.ForeignKey('Temperature', on_delete=models.CASCADE)
    nitric_oxide = models.DecimalField(max_digits=None, decimal_places=1)
    nitrogen_dioxide = models.DecimalField(max_digits=None, decimal_places=1)
    nitrogen_oxides = models.DecimalField(max_digits=None, decimal_places=1)
    pm10 = models.DecimalField(max_digits=None, decimal_places=1)
    pm2point5 = models.DecimalField(max_digits=None, decimal_places=1)
    pm1 = models.DecimalField(max_digits=None, decimal_places=1)
    ozone = models.DecimalField(max_digits=None, decimal_places=1)
"""