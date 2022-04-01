from django.shortcuts import redirect, render, get_object_or_404
from .models import Station_data, Station_details
from django.core.paginator import Paginator
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.graph_objs import Scatter
import plotly.express as px
import pandas as pd
import numpy as np


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

    x_data = [row.id for row in data]
    above = 0
    avg = 0
    avg_list = []
    if request.POST.get('chart_type') == "nitrogen_dioxide":
        y_data = [row.nitrogen_dioxide for row in data] #[f"{row}.{variable}" for row in data]
        for row in data:
            try:
                row.nitrogen_dioxide = float(row.nitrogen_dioxide)
                print(row.nitrogen_dioxide)
                if row.nitrogen_dioxide > 25:
                    above += 1
                avg_list.append(row.nitrogen_dioxide)
            except:
                pass
        try:
            avg = round(sum(avg_list) / len(avg_list), 2)
        except ZeroDivisionError:
            avg = 0
    elif request.POST.get('chart_type') == "nitrogen_oxides":
        y_data = [row.nitrogen_oxides for row in data]
        for row in data:
            try:
                row.nitrogen_oxides = float(row.nitrogen_oxides)
                if row.nitrogen_oxides > 25:
                    above += 1
                avg_list.append(row.nitrogen_oxides)
            except:
                pass
        try:
            avg = round(sum(avg_list) / len(avg_list), 2)
        except ZeroDivisionError:
            avg = 0
    elif request.POST.get('chart_type') == "pm10":
        y_data = [row.pm10 for row in data]
        for row in data:
            try:
                row.pm10 = float(row.pm10)
                if row.pm10 > 45:
                    above += 1
                avg_list.append(row.pm10)
            except:
                pass
        try:
            avg = round(sum(avg_list) / len(avg_list), 2)
        except ZeroDivisionError:
            avg = 0
    elif request.POST.get('chart_type') == "pm2point5":
        y_data = [row.pm2point5 for row in data]
        for row in data:
            try:
                row.pm2point5 = float(row.pm2point5)
                if row.pm2point5 > 15:
                    above += 1
                avg_list.append(row.pm2point5)
            except:
                pass
        try:
            avg = round(sum(avg_list) / len(avg_list), 2)
        except ZeroDivisionError:
            avg = 0
    elif request.POST.get('chart_type') == "nitric_oxide":
        y_data = [row.nitric_oxide for row in data]
        for row in data:
            try:
                row.nitric_oxide = float(row.nitric_oxide)
                if row.nitric_oxide > 25:
                    above += 1
                avg_list.append(row.nitric_oxide)
            except:
                pass
        try:
            avg = round(sum(avg_list) / len(avg_list), 2)
        except ZeroDivisionError:
            avg = 0
    else:
        y_data = [row.nitrogen_dioxide for row in data]
        for row in data:
            try:
                row.nitrogen_dioxide = float(row.nitrogen_dioxide)
                print(row.nitrogen_dioxide)
                if row.nitrogen_dioxide > 25:
                    above += 1
                avg_list.append(row.nitrogen_dioxide)
            except:
                pass
        try:
            avg = round(sum(avg_list) / len(avg_list), 2)
        except ZeroDivisionError:
            avg = 0

    plot_div = plot([Scatter(x=x_data, y=y_data,
                                    mode='lines', name='test',
                                    opacity=0.8, marker_color='green')],
                                    output_type='div')

    """
    ni_di_list = []
    for row in data:
        ni_di = row.variable
        ni_di_list.append(ni_di)
    print(ni_di_list)
    #avg = sum(ni_di_list) / len(ni_di_list)
    #print(avg, "is the average")
    """

    """
    df = pd.read_sql_query('SELECT *
                           'FROM air_tracker_station_data '
                           'WHERE station_details_id=station'
                           , disk_engine)

                Station_data.objects.filter(station_details_id=station)
            """

    """
    trace1 = go.Scatter(
        x=x_data, y=ni_di_list,
        mode='lines', name='f(x)', marker=dict(
            color='rgb(220, 20, 60)'
        )
    )
    trace2 = go.Scatter(
        x=x_data, y=ni_di_list + 1,
        mode='lines',
        name='g(x)',
        marker=dict(
            color='rgb(100, 149, 237)'
        )
    )

    plot_div2 = plot([Scatter(x=x_data, y=df.columns[3:4],
                              mode='lines', name='test',
                              opacity=0.8, marker_color='green')],
                     output_type='div')
    """

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
        #'plot_div2': plot_div2,
        'variable': request.POST.get('chart_type'),
        'above': above,
        'avg': avg,
        'station_id_num': station_id_num,
    }
    return render(request, 'air_tracker/data.html', context)
