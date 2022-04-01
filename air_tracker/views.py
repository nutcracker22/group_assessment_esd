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
    station_id_num = Station_details.objects.all().order_by("id")
    data = Station_data.objects.filter(station_details_id=station)
    ni_di_list = []
    if request.POST.get('chart_type') == "nitrogen_dioxide":
        variable = 'nitrogen_dioxide'
        for row in data:
            ni_di = f"{row}.{variable}"
            ni_di_list.append(ni_di)
        x_data = [row.id for row in data]
        y_data = [row.nitrogen_dioxide for row in data] #[f"{row}.{variable}" for row in data]
        plot_div = plot([Scatter(x=x_data, y=y_data,
                                        mode='lines', name='test',
                                        opacity=0.8, marker_color='green')],
                                        output_type='div')
    elif request.POST.get('chart_type') == "nitrogen_oxides":
        variable = 'nitrogen_oxides'
        for row in data:
            ni_di = f"{row}.{variable}"
            ni_di_list.append(ni_di)
        x_data = [row.id for row in data]
        y_data = [row.nitrogen_oxides for row in data] #[f"{row}.{variable}" for row in data]
        plot_div = plot([Scatter(x=x_data, y=y_data,
                                        mode='lines', name='test',
                                        opacity=0.8, marker_color='green')],
                                        output_type='div')
    elif request.POST.get('chart_type') == "pm10":
        variable = 'pm10'
        for row in data:
            ni_di = f"{row}.{variable}"
            ni_di_list.append(ni_di)
        x_data = [row.id for row in data]
        y_data = [row.pm10 for row in data] #[f"{row}.{variable}" for row in data]
        plot_div = plot([Scatter(x=x_data, y=y_data,
                                        mode='lines', name='test',
                                        opacity=0.8, marker_color='green')],
                                        output_type='div')
    elif request.POST.get('chart_type') == "pm2point5":
        variable = "pm2point5"
        for row in data:
            ni_di = f"{row}.{variable}"
            ni_di_list.append(ni_di)
        x_data = [row.id for row in data]
        y_data = [row.pm2point5 for row in data] #[f"{row}.{variable}" for row in data]
        plot_div = plot([Scatter(x=x_data, y=y_data,
                                        mode='lines', name='test',
                                        opacity=0.8, marker_color='green')],
                                        output_type='div')
    elif request.POST.get('chart_type') == "nitric_oxide":
        variable = "nitric_oxide"
        for row in data:
            ni_di = f"{row}.{variable}"
            ni_di_list.append(ni_di)
        x_data = [row.id for row in data]
        y_data = [row.nitric_oxide for row in data] #[f"{row}.{variable}" for row in data]
        plot_div = plot([Scatter(x=x_data, y=y_data,
                                        mode='lines', name='test',
                                        opacity=0.8, marker_color='green')],
                                        output_type='div')
    else:
        variable = 'nitrogen_dioxide'
        for row in data:
            ni_di = f"{row}.{variable}"
            ni_di_list.append(ni_di)
        x_data = [row.id for row in data]
        y_data = [row.nitrogen_dioxide for row in data] #[f"{row}.{variable}" for row in data]
        plot_div = plot([Scatter(x=x_data, y=y_data,
                                        mode='lines', name='test',
                                        opacity=0.8, marker_color='green')],
                                        output_type='div')
    """
    for row in data:
        ni_di = f"{row}.{variable}"
        ni_di_list.append(ni_di)
    x_data = [row.id for row in data]
    y_data = [row.nitric_oxide for row in data] #[f"{row}.{variable}" for row in data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                                    mode='lines', name='test',
                                    opacity=0.8, marker_color='green')],
                                    output_type='div')
    """
    #print(ni_di)
    #date = data.date.date
    #print(date)

    if station != None:
        station_name = get_object_or_404(Station_details, id=station)
    else:
        station_name = None

    paginator = Paginator(data, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'station': station, 
        'station_name': station_name,
        'plot_div': plot_div,
        'variable': variable,
        'station_id_num': station_id_num,
    }
    return render(request, 'air_tracker/data.html', context)
