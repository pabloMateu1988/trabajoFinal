from django.contrib import admin
from alumnos.models import Alumno,Materia,Notas

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    search_fields = (('nombre','dni'))
    date_hierarchy = 'insc_date'
    list_display = ('dni','nombre','insc_date')
    pass

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    pass
@admin.register(Notas)
class NotasAdmin(admin.ModelAdmin):
    list_display = ('alumno','materia','calificacion','exam_date')
    pass

# Register your models here.
