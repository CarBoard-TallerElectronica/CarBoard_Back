from .logic import logic_nodo
from django.core import serializers
from django.shortcuts import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


def node_list(request):
    if request.method == 'GET':
        nodos = logic_nodo.get_nodos()
        nodos_dto = serializers.serialize('json', nodos)

        return HttpResponse(nodos_dto, content_type='application/json')


def nodo(request, pk):
    if request.method == 'GET':
        nodo = logic_nodo.get_nodo_ID(pk)
        nodo_dto = serializers.serialize('json',[nodo])

        return HttpResponse(nodo_dto, content_type='application/json')
    
@csrf_exempt
def registrar_nodo(request):
    if request.method == 'POST':
        nodo_dto = logic_nodo.register_nodo(json.loads(request.body))
        nodo = serializers.serialize('json', [nodo_dto])

        return HttpResponse(nodo, content_type='application/json')