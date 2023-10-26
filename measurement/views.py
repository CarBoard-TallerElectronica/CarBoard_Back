from django.shortcuts import render
from .logic import logic_measure
from django.shortcuts import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def measurement_list(request):
    if request.method == 'GET':
        citas = logic_measure.get_measurements()
        citas_dto = serializers.serialize('json', citas)
    return HttpResponse(citas_dto, content_type='application/json')


#def measurement():


#@csrf_exempt
#def log_measurment(request):

