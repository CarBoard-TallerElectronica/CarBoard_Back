from ..models import Measurement
from ..models import Nodo
from datetime import datetime

def get_measurements():
    return Measurement.objects.all()

def get_measurement_ID(id_pk):
    measurement = Measurement.objects.get(pk=id_pk)
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
            year= data['year'],
            month= data['month'],
            day= data['day'],
            hour= data['hour'],
            minute= data['minute'],
            second= data['second']
        )
    )
    
    if measurement.timestamp_components_valid():
        measurement.timestamp = measurement._create_timestamp()

    measurement.save()

    return measurement
