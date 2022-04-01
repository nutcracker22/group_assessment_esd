import csv
from multiprocessing.sharedctypes import Value
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from air_tracker.models import Station_details, Dates, Times, Wind_direction, Wind_speed, Temperature, Station_data
from . import scraper

class Command(BaseCommand):
    def handle(self, *args, **options):
        #drop all tables to prevent duplicates
        Station_details.objects.all().delete()
        Dates.objects.all().delete()
        Times.objects.all().delete()
        Wind_direction.objects.all().delete()
        Wind_speed.objects.all().delete()
        Temperature.objects.all().delete()
        Station_data.objects.all().delete()
        print("Table dropped successfully")
        base_dir = Path(__file__).resolve().parent.parent.parent.parent

        #call scraper
        with open(f'{base_dir}/air_tracker/data/station_details.csv', 'r') as file:
            csvFile = csv.reader(file, delimiter=",")
            next(csvFile)
            for lines in csvFile:
                site_name = lines[0]
                site_type = lines[1]
                print(lines[2])
                latitude = float(lines[2].split(",")[0])
                longitude = float(lines[3])
                site_comment = lines[4]

                station_details = Station_details.objects.create(
                    site_name=site_name,
                    site_type=site_type,
                    latitude=latitude,
                    longitude=longitude,
                    site_comments=site_comment,
                )
                station_details.save()

        #if no data
        wind_direction = Wind_direction.objects.create(direction = -1)
        wind_direction.save()
        wind_speed = Wind_speed.objects.create(speed = -1)
        wind_speed.save()
        temperature = Temperature.objects.create(temp = -1)
        temperature.save()

        count = 4

        with open(f'{base_dir}/air_tracker/data/air_pollution_data.csv', "r") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)    #skip station name
            next(reader)    #skip date,time,nitric oxide line
            for row in reader:
                print(count)
                count += 1
                #change date to iso format
                dd,mm,yy = row[0][0:2],row[0][3:5],row[0][6:10]
                date = f'{yy}-{mm}-{dd}'
                try:
                    dates = Dates.objects.create(date = date)
                    dates.save()
                except IntegrityError:
                    pass

                try:
                    time_in_row = row[1]
                    if time_in_row == '24:00':
                        time_in_row = '00:00'
                        times = Times.objects.create(time = time_in_row)
                        times.save() 
                    else:
                        times = Times.objects.create(time = row[1])
                        times.save()
                except IntegrityError:
                    pass

                #parse wind direction of each rows
                index = 14
                while index<105:
                    try:
                        wind_direction = Wind_direction.objects.create(direction = round(float(row[index])))
                        wind_direction.save()
                    except ValueError:
                        pass
                    except IntegrityError:
                        pass
                    index += 18
                
                #parse wind speed of each rows
                index = 16
                while index<107:
                    try:
                        wind_speed = Wind_speed.objects.create(speed = float(row[index]))
                        wind_speed.save()
                    except ValueError:
                        pass
                    except IntegrityError:
                        pass
                    index += 18

                #parse temperature of each rows
                index = 18
                while index<109:
                    try:
                        temperature = Temperature.objects.create(temp = float(row[index]))
                        temperature.save()
                    except ValueError:
                        pass
                    except IntegrityError:
                        pass
                    index += 18
                
                #input into Station_data ANDERSON DR
                site_name='Aberdeen Anderson Dr'
                date = date
                time=time_in_row,
                try:
                    direction=round(float(row[14]))
                except ValueError:
                    direction = -1
                try:
                    speed=float(row[16])
                except ValueError:
                    speed = -1
                try:
                    temp=float(row[18])
                except ValueError:
                    temp = -1
                try:
                    nitric_oxide = float(row[2])
                except ValueError:
                    nitric_oxide= None
                try:
                    nitrogen_dioxide = float(row[4])
                except ValueError:
                    nitrogen_dioxide= None
                try:
                    nitrogen_oxides = float(row[6])
                except ValueError:
                    nitrogen_oxides= None
                try:
                    pm10 = float(row[8])
                except ValueError:
                    pm10= None
                try:
                    pm2point5 = float(row[10])
                except ValueError:
                    pm2point5= None

                station = Station_data.objects.create(
                    station_details = Station_details.objects.get(site_name=site_name),
                    date = Dates.objects.get(date=date),
                    time = Times.objects.get(time=time_in_row),
                    wind_direction = Wind_direction.objects.get(direction=direction),
                    wind_speed = Wind_speed.objects.get(speed=speed),
                    temperature = Temperature.objects.get(temp=temp),
                    nitric_oxide = nitric_oxide,
                    nitrogen_dioxide = nitrogen_dioxide,
                    nitrogen_oxides = nitrogen_oxides,
                    pm10 = pm10,
                    pm2point5 = pm2point5,
                    #pm1 = float(row[12])
                )
                station.save()

                #INPUT INTO ERROLL PARK
                site_name='Aberdeen Erroll Park'
                date = date
                time=time_in_row,
                try:
                    direction=round(float(row[32]))
                except ValueError:
                    direction = -1
                try:
                    speed=float(row[34])
                except ValueError:
                    speed = -1
                try:
                    temp=float(row[36])
                except ValueError:
                    temp = -1
                try:
                    nitric_oxide = float(row[22])
                except ValueError:
                    nitric_oxide= None
                try:
                    nitrogen_dioxide = float(row[24])
                except ValueError:
                    nitrogen_dioxide= None
                try:
                    nitrogen_oxides = float(row[26])
                except ValueError:
                    nitrogen_oxides= None
                try:
                    pm10 = float(row[28])
                except ValueError:
                    pm10= None
                try:
                    pm2point5 = float(row[30])
                except ValueError:
                    pm2point5= None

                station = Station_data.objects.create(
                    station_details = Station_details.objects.get(site_name=site_name),
                    date = Dates.objects.get(date=date),
                    time = Times.objects.get(time=time_in_row),
                    wind_direction = Wind_direction.objects.get(direction=direction),
                    wind_speed = Wind_speed.objects.get(speed=speed),
                    temperature = Temperature.objects.get(temp=temp),
                    nitric_oxide = nitric_oxide,
                    nitrogen_dioxide = nitrogen_dioxide,
                    nitrogen_oxides = nitrogen_oxides,
                    pm10 = pm10,
                    pm2point5 = pm2point5,
                    #pm1 = float(row[12])
                )
                station.save()

                #INPUT INTO KING ST
                site_name='Aberdeen King Street'
                date = date
                time=time_in_row,
                try:
                    direction=round(float(row[50]))
                except ValueError:
                    direction = -1
                try:
                    speed=float(row[52])
                except ValueError:
                    speed = -1
                try:
                    temp=float(row[54])
                except ValueError:
                    temp = -1
                try:
                    nitric_oxide = float(row[38])
                except ValueError:
                    nitric_oxide= None
                try:
                    nitrogen_dioxide = float(row[40])
                except ValueError:
                    nitrogen_dioxide= None
                try:
                    nitrogen_oxides = float(row[42])
                except ValueError:
                    nitrogen_oxides= None
                try:
                    pm10 = float(row[44])
                except ValueError:
                    pm10= None
                try:
                    pm2point5 = float(row[46])
                except ValueError:
                    pm2point5= None

                station = Station_data.objects.create(
                    station_details = Station_details.objects.get(site_name=site_name),
                    date = Dates.objects.get(date=date),
                    time = Times.objects.get(time=time_in_row),
                    wind_direction = Wind_direction.objects.get(direction=direction),
                    wind_speed = Wind_speed.objects.get(speed=speed),
                    temperature = Temperature.objects.get(temp=temp),
                    nitric_oxide = nitric_oxide,
                    nitrogen_dioxide = nitrogen_dioxide,
                    nitrogen_oxides = nitrogen_oxides,
                    pm10 = pm10,
                    pm2point5 = pm2point5,
                    #pm1 = float(row[12])
                )
                station.save()

                #INPUT INTO MARKET STREET2
                site_name='Aberdeen Market Street 2'
                date = date
                time=time_in_row,
                try:
                    direction=round(float(row[68]))
                except ValueError:
                    direction = -1
                try:
                    speed=float(row[70])
                except ValueError:
                    speed = -1
                try:
                    temp=float(row[72])
                except ValueError:
                    temp = -1
                try:
                    nitric_oxide = float(row[56])
                except ValueError:
                    nitric_oxide= None
                try:
                    nitrogen_dioxide = float(row[58])
                except ValueError:
                    nitrogen_dioxide= None
                try:
                    nitrogen_oxides = float(row[60])
                except ValueError:
                    nitrogen_oxides= None
                try:
                    pm10 = float(row[62])
                except ValueError:
                    pm10= None
                try:
                    pm2point5 = float(row[64])
                except ValueError:
                    pm2point5= None

                station = Station_data.objects.create(
                    station_details = Station_details.objects.get(site_name=site_name),
                    date = Dates.objects.get(date=date),
                    time = Times.objects.get(time=time_in_row),
                    wind_direction = Wind_direction.objects.get(direction=direction),
                    wind_speed = Wind_speed.objects.get(speed=speed),
                    temperature = Temperature.objects.get(temp=temp),
                    nitric_oxide = nitric_oxide,
                    nitrogen_dioxide = nitrogen_dioxide,
                    nitrogen_oxides = nitrogen_oxides,
                    pm10 = pm10,
                    pm2point5 = pm2point5,
                    #pm1 = float(row[12])
                )
                station.save()

                #INPUT INTO UNION ST
                site_name='Aberdeen Union Street Roadside'
                date = date
                time=time_in_row,
                try:
                    direction=round(float(row[86]))
                except ValueError:
                    direction = -1
                try:
                    speed=float(row[88])
                except ValueError:
                    speed = -1
                try:
                    temp=float(row[90])
                except ValueError:
                    temp = -1
                try:
                    nitric_oxide = float(row[74])
                except ValueError:
                    nitric_oxide= None
                try:
                    nitrogen_dioxide = float(row[76])
                except ValueError:
                    nitrogen_dioxide= None
                try:
                    nitrogen_oxides = float(row[78])
                except ValueError:
                    nitrogen_oxides= None
                try:
                    pm10 = float(row[80])
                except ValueError:
                    pm10= None
                try:
                    pm2point5 = float(row[82])
                except ValueError:
                    pm2point5= None

                station = Station_data.objects.create(
                    station_details = Station_details.objects.get(site_name=site_name),
                    date = Dates.objects.get(date=date),
                    time = Times.objects.get(time=time_in_row),
                    wind_direction = Wind_direction.objects.get(direction=direction),
                    wind_speed = Wind_speed.objects.get(speed=speed),
                    temperature = Temperature.objects.get(temp=temp),
                    nitric_oxide = nitric_oxide,
                    nitrogen_dioxide = nitrogen_dioxide,
                    nitrogen_oxides = nitrogen_oxides,
                    pm10 = pm10,
                    pm2point5 = pm2point5,
                    #pm1 = float(row[12])
                )
                station.save()

                #INPUT INTO WELLINGTON RD
                site_name='Aberdeen Wellington Road'
                date = date
                time=time_in_row,
                try:
                    direction=round(float(row[104]))
                except ValueError:
                    direction = -1
                try:
                    speed=float(row[106])
                except ValueError:
                    speed = -1
                try:
                    temp=float(row[108])
                except ValueError:
                    temp = -1
                try:
                    nitric_oxide = float(row[92])
                except ValueError:
                    nitric_oxide= None
                try:
                    nitrogen_dioxide = float(row[94])
                except ValueError:
                    nitrogen_dioxide= None
                try:
                    nitrogen_oxides = float(row[96])
                except ValueError:
                    nitrogen_oxides= None
                try:
                    pm10 = float(row[98])
                except ValueError:
                    pm10= None
                try:
                    pm2point5 = float(row[100])
                except ValueError:
                    pm2point5= None

                station = Station_data.objects.create(
                    station_details = Station_details.objects.get(site_name=site_name),
                    date = Dates.objects.get(date=date),
                    time = Times.objects.get(time=time_in_row),
                    wind_direction = Wind_direction.objects.get(direction=direction),
                    wind_speed = Wind_speed.objects.get(speed=speed),
                    temperature = Temperature.objects.get(temp=temp),
                    nitric_oxide = nitric_oxide,
                    nitrogen_dioxide = nitrogen_dioxide,
                    nitrogen_oxides = nitrogen_oxides,
                    pm10 = pm10,
                    pm2point5 = pm2point5,
                    #pm1 = float(row[12])
                )
                station.save()
                """
                station = Station_data.objects.create(
                    station_details = Station_details.objects.get(site_name='Aberdeen Anderson Dr'),
                    date = Dates.objects.get(date=date),
                    time = Times.objects.get(time=time_in_row),
                    wind_direction = Wind_direction.objects.get(direction=round(float(row[14]))),
                    wind_speed = Wind_speed.objects.get(speed=float(row[16])),
                    temperature = Temperature.objects.get(temp=float(row[18])),
                    nitric_oxide = float(row[2]),
                    nitrogen_dioxide = float(row[4]),
                    nitrogen_oxides = float(row[6]),
                    pm10 = float(row[8]),
                    pm2point5 = float(row[10]),
                    #pm1 = float(row[12])
                )
                station.save()

                station = Station_data.objects.create(
                    station_details = Station_details.objects.get(site_name='Aberdeen Erroll Park'),
                    date = Dates.objects.get(date=date),
                    time = Times.objects.get(time=time_in_row),
                    wind_direction = Wind_direction.objects.get(direction=round(float(row[32]))),
                    wind_speed = Wind_speed.objects.get(speed=float(row[34])),
                    temperature = Temperature.objects.get(temp=float(row[36])),
                    nitric_oxide = float(row[22]),
                    nitrogen_dioxide = float(row[24]),
                    nitrogen_oxides = float(row[26]),
                    pm10 = float(row[28]),
                    pm2point5 = float(row[30])
                    #pm1 = float(row[12])
                )
                station.save()
                """

                """
                wind_speed = Wind_speed.objects.create(speed = float(row[34]))
                wind_speed.save()
                wind_speed = Wind_speed.objects.create(speed = float(row[52]))
                wind_speed.save()
                wind_speed = Wind_speed.objects.create(speed = float(row[70]))
                wind_speed.save()
                wind_speed = Wind_speed.objects.create(speed = float(row[88]))
                wind_speed.save()
                wind_speed = Wind_speed.objects.create(speed = float(row[106]))
                wind_speed.save()

                temperature = Temperature.objects.create(temp = float(row[18]))
                temperature.save()
                temperature = Temperature.objects.create(temp = float(row[36]))
                temperature.save()
                temperature = Temperature.objects.create(temp = float(row[54]))
                temperature.save()
                temperature = Temperature.objects.create(temp = float(row[72]))
                temperature.save()
                temperature = Temperature.objects.create(temp = float(row[90]))
                temperature.save()
                temperature = Temperature.objects.create(temp = float(row[108]))
                temperature.save()
                """