from django.shortcuts import render
from .models import Station_data
from django.core.paginator import Paginator


def home(request):
    context = {

    }
    return render(request, 'air_tracker/home.html', context)


def login(request):
    pass


def info(request):
    return render(request, 'air_tracker/info.html')


def data_page(request):
    station = None
    data = Station_data.objects.all().filter(station_details_id=1)
    paginator = Paginator(data, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        station = request.POST.get('station_name')

    return render(request, 'air_tracker/data.html', {'page_obj': page_obj, 'station': station})


