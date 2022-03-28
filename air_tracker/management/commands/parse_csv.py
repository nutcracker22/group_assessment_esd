import csv
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
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
        with open(f'{base_dir}/air_tracker/data/air_pollution_data.csv', "r") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)    #skip header
            next(reader)
            for row in reader:
                """
                station_details = Station_details.objects.create(
                    site_name = 
                )
                """
                #change date to iso format
                dd,mm,yy = row[0][0:2],row[0][3:5],row[0][6:10]
                date = f'{yy}-{mm}-{dd}'
                dates = Dates.objects.create(date = date)
                dates.save()

                times = Times.objects.create(time = row[1])
                times.save()

                wind_direction = Wind_direction.objects.create(direction = int(row[16]))
                wind_direction.save()

                wind_speed = Wind_speed.objects.create(speed = float(row[18]))
                wind_speed.save()

                temperature = Temperature.objects.create(temp = float(row[20]))
                temperature.save()

        scraper.scrape_starter()
        scraper.finishing()