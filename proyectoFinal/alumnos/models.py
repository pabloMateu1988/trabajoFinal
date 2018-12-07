from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False, default='')
    insc_date = models.DateField("Fecha de Inscripción", max_length=255, blank=False)
    dni = models.CharField(max_length=255, blank=False, null=False,default='')
    class Meta:
        verbose_name_plural = "Alumnos"
        verbose_name = "Alumno"
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField("Nombre",max_length=255, blank=False, null=False)
    #alumnos = models.ManyToManyField(Alumno, through='Notas')
    class Meta:
        verbose_name_plural = "Materias"
        verbose_name = "Materia"
    def __str__(self):
        return self.nombre


class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    exam_date = models.DateField("Fecha de Examen", blank=False, null=False)
    calificacion = models.IntegerField(blank=False,null=False)
    class Meta:
        verbose_name_plural = "Notas"
        verbose_name = "Nota"
    def __str__(self):
        return str(self.alumno) + ' - ' + str(self.materia) + ' - ' + str(self.calificacion)