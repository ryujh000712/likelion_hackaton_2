from django.urls import admin
from django.urls import path
from . import views

urlpatterns = [
  pah('',views.portfolio, name = 'portfolio'),

]