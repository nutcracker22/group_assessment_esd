from django.shortcuts import redirect, render, get_object_or_404
from .models import Station_data, Station_details
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
    if 'station_name' in request.session:
        station = request.session['station_name']
    else:
        request.session['station_name']=station
    request.session.modified = True

    if request.method == "POST":
        station = request.POST.get('station_name')
        request.session['station_name'] = station

    data = Station_data.objects.all().filter(station_details_id=station)

    if station != None:
        station_name = get_object_or_404(Station_details, id=station)
    else:
        station_name = None
    paginator = Paginator(data, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'air_tracker/data.html', {'page_obj': page_obj, 'station': station, 'station_name': station_name})

# def data_page(request):
#     station = None
#     data = Station_data.objects.all().filter(station_details_id=1)
#     paginator = Paginator(data, 40)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     if request.method == "POST":
#         station = request.POST.get('station_name')
#
#     return render(request, 'air_tracker/data.html', {'page_obj': page_obj, 'station': station})


