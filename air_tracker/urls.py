from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.data_page, name='data_page'),
    path('about-air-pollution/', views.info, name='info'),
    path('search/', views.search, name='search'),
]