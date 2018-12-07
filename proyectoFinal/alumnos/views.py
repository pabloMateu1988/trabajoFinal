# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from alumnos.models import Alumno
from alumnos.serializers import AlumnoSerializer

@csrf_exempt
def alumno_list(request):
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