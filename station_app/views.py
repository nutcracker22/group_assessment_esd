from django.shortcuts import render

def home(request):
    context = {

    }
    return render(request, 'station_app/home.html', context)