from django.contrib import admin
from .models import Station_details, Dates, Times, Wind_direction, Wind_speed, Temperature#, Station_data
# Register your models here.

admin.site.register(Station_details)
admin.site.register(Dates)
admin.site.register(Times)
admin.site.register(Wind_direction)
admin.site.register(Wind_speed)
admin.site.register(Temperature)
#admin.site.register(Station_data)