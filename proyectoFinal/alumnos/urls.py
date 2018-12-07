from django.urls import path
from alumnos import views

from . import views

urlpatterns = [
    path('alumnos/',views.alumno_list),
]