import json
from django.shortcuts import render
from .logic import logic_measure
from django.shortcuts import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def measurement_list(request):
    if request.method == 'GET':
        measurements = logic_measure.get_measurements()
        measurements_dto = serializers.serialize('json', measurements)
        return HttpResponse(measurements_dto, content_type='application/json')


def measurement(request, pk):
    if request.method == 'GET':
        measuremet = logic_measure.get_measurement_ID(pk)
        measuremet_dto = serializers.serialize('json', [measuremet])
        return HttpResponse(measuremet_dto, content_type='application/json')
    

def measurementNodo(request, nd):
    if request.method == 'GET':
        measurements = logic_measure.get_measurementsNodo(nd)
        measurements_dto = serializers.serialize('json', measurements)
        return HttpResponse(measurements_dto, content_type='application/json')
    

def latestMeasurementNodo(request, nd):
    if request.method == 'GET':
        measurement = logic_measure.get_measurementsNodo(nd).latest('timestamp')
        return HttpResponse(measurement, content_type='application/json')

@csrf_exempt
def log_measurment(request):
    if request.method == 'POST':
        measurement_dto = logic_measure.log_measurement(json.loads(request.body))
        measuremet = serializers.serialize('json', [measurement_dto])
        return HttpResponse(measuremet, content_type='application/json')
