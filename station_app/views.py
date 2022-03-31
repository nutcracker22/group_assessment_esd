from django.shortcuts import render, redirect, get_object_or_404
from air_tracker.models import Station_details, Station_data
from django.core.paginator import Paginator

def home(request):
    stations = Station_details.objects.all()
    context = {
        'stations':stations,
    }
    return render(request, 'station_app/home.html', context)

def details(request, id):
    station = get_object_or_404(Station_details, id=id)
    #data = Station_data.objects.filter(station_details_id=id)
    request.session["station_name"]=station.id
    
    context = {
        'station':station,
    }
    return render(request, 'station_app/details.html', context)
