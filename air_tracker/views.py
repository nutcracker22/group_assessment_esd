from django.shortcuts import redirect, render, get_object_or_404
from .models import Station_data, Station_details
from django.core.paginator import Paginator
from plotly.offline import plot
from plotly.graph_objs import Scatter


def home(request):
    request.session['station_name'] = None
    return redirect('station_app:home')


def info(request):
    request.session['station_name'] = None
    return render(request, 'air_tracker/info.html')

def search(request):
    station = None
    search = None
    if request.method == "POST":
        search = request.POST.get("search")
    station = Station_details.objects.filter(site_name__iregex=fr"{search}+")
    return render(request, 'air_tracker/search.html', {'station':station, 'search':search})

def data_page(request):
    station = None
    if 'station_name' in request.session:
        station = request.session['station_name']
    else:
        request.session['station_name'] = None
    request.session.modified = True

    if request.method == "POST":
        station = request.POST.get('station_name')
        request.session['station_name'] = station

    data = Station_data.objects.all().filter(station_details_id=station)
    ni_di_list = []
    for row in data:
        ni_di = row.nitrogen_dioxide
        ni_di_list.append(ni_di)
    #print(ni_di)
    #date = data.date.date
    #print(date)

    if station != None:
        station_name = get_object_or_404(Station_details, id=station)
    else:
        station_name = None

    x_data = [row.id for row in data]
    y_data = [row.nitrogen_dioxide for row in data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                             mode='lines', name='test',
                             opacity=0.8, marker_color='green')],
                             output_type='div')

    paginator = Paginator(data, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'station': station, 
        'station_name': station_name,
        'plot_div': plot_div
    }
    return render(request, 'air_tracker/data.html', context)
