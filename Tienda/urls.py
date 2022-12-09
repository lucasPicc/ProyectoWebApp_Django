from django.urls import path
from Tienda.views import *

urlpatterns = [
    path('', tienda, name="Tienda"),
]
