from ..models import Nodo

def get_nodos():
    return Nodo.objects.all()

def get_nodo_ID(id_pk):
    nodo = Nodo.objects.get(pk=id_pk)
    return nodo

def register_nodo(data):

    nodo  = Nodo(usuario = data['usuario'], 
                 modelo = data['modelo'],
                 anio = data['anio'])

    nodo.save()
    
    return nodo