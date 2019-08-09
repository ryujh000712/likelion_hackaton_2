from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.wchome, name = 'wchome'),
    path('about/',views.about, name = 'about'),
    path('count/',views.count, name = 'count'),
]