from ..models import Measurement
from ..models import Nodo
from datetime import datetime

def get_measurements():
    return Measurement.objects.all()

def get_measurement_ID(id_pk):
    measurement = Measurement.objects.get(pk=id_pk)
    return measurement

def get_measurementsNodo(id_nd):
    nodo = Nodo.objects.get(pk=id_nd)
    measurement = Measurement.objects.filter(nodo=nodo)
    return measurement

def log_measurement(data):
    nodo = Nodo.objects.get(pk=data['nodo'])

    measurement = Measurement(
        nodo=nodo,
        latitud=data['latitud'],
        longitud=data['longitud'],
        velocidad=data['velocidad'],
        aceleracion=data['aceleracion'],
        azimuth=data['azimuth'],
        positionDOP=data['positionDOP'],
        timestamp= datetime(
            year= data['time']['year'],
            month= data['time']['month'],
            day= data['time']['day'],
            hour= data['time']['hour'],
            minute= data['time']['minute'],
            second= data['time']['second']
        )
    )


    measurement.save()

    return measurement
