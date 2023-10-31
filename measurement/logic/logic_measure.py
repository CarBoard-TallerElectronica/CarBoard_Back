from ..models import Measurement
from ..models import Nodo

def get_measurements():
    return Measurement.objects.all()

def get_measurement_ID(id_pk):
    measurement = Measurement.objects.get(pk=id_pk)
    return measurement

def log_measurement(data):

    nodo =  Nodo.objects.get(pk=data['nodo'])
    measurement = Measurement(nodo= nodo, 
                              latitud= data['latitud'], 
                              longitud= data['longitud'], 
                              velocidad= data['velocidad'], 
                              aceleracion= data['aceleracion'])

    measurement.save()


    return measurement