from django.shortcuts import render
# from .models import Station_data
# from django.core.paginator import Paginator


def home(request):
    context = {

    }
    return render(request, 'air_tracker/home.html', context)


def login(request):
    pass


def info(request):
    return render(request, 'air_tracker/info.html')


def data_page(request):
    # data = Station_data.objects.all()
    # paginator = Paginator(data, 50)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    return render(request, 'air_tracker/data.html')


