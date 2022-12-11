from django.urls import path
from .views import *

urlpatterns = [
    path('', Vregistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_session, name="cerrar_sesion"),
    path('loguear', loguear, name="loguear"),
]
