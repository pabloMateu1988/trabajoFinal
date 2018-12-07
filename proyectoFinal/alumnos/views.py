# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from alumnos.models import Alumno,Materia,Nota
from alumnos.serializers import AlumnoSerializer, MateriaSerializer, NotaSerializer

@csrf_exempt
def alumnos_list(request):
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return JsonResponse(serializer.data, safe=False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = AlumnoSerializer(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status = 201)
    #     return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def materias_list(request):
    if request.method == 'GET':
        materias = Materia.objects.all()
        serializer = MateriaSerializer(materias, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def notas_list(request):
    if request.method == 'GET':
        notas = Nota.objects.all()
        serializer = NotaSerializer(notas, many=True)
        return JsonResponse(serializer.data, safe=False)