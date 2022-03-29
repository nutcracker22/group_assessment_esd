import csv
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from air_tracker.models import Station_details, Dates, Times, Wind_direction, Wind_speed, Temperature#, Station_data
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
        #Station_data.objects.all().delete()
        print("Table dropped successfully")

        #call scraper
        scraper.scrape_starter()
        scraper.finishing()

        count = 4
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
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
                    if row[1] == '24:00':
                        times = Times.objects.create(time = '00:00')
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