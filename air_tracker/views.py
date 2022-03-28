from django.shortcuts import render

def home(request):
    context = {

    }
    return render(request, 'air_tracker/home.html', context)
