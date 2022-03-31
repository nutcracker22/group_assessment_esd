from django.contrib import admin
from django.urls import path
from . import views

app_name = 'station_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/', views.details, name='details'),
]