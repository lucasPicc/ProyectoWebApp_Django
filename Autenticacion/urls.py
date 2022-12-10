from django.urls import path
from .views import *

urlpatterns = [
    path('', Vregistro.as_view(), name="Autenticacion"),
]
