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
    data = Station_data.objects.filter(station_details_id=id)
    paginator = Paginator(data, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'station':station,
        'page_obj':page_obj,
    }
    return render(request, 'station_app/details.html', context)
