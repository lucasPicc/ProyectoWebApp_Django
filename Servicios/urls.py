from django.urls import path
from .views import *

urlpatterns = [
    path('', servicios, name="Servicios"),
]
