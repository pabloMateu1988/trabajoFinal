from django.urls import path
from alumnos import views

from . import views

urlpatterns = [
    path('alumnos/',views.alumnos_list),
    path('materias/',views.materias_list),
    path('notas/',views.notas_list),
]