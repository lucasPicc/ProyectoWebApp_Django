from django.urls import path
from ProyectoWebApp.views import *

urlpatterns = [
    path('', home, name="Home"),
    path('tienda/', tienda, name="Tienda"),
]
