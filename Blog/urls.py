from django.urls import path
from .views import *

urlpatterns = [
    path('', blog, name="Blog"),
    path('categoria/<int:categoria_id>', categoria, name="Categoria"),
]