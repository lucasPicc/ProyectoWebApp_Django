from django.urls import path
from .views import *

urlpatterns = [
    path('', procesar_pedido, name="Procesar_pedido"),
]
