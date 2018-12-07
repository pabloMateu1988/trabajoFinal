# Generated by Django 2.1.3 on 2018-12-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0004_auto_20181207_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='insc_date',
            field=models.DateField(max_length=255, verbose_name='Fecha de Inscripción'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
    ]
