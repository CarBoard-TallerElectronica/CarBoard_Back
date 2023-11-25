from django.db import models
from nodo.models import Nodo

class Measurement(models.Model):

    nodo = models.ForeignKey(Nodo, on_delete=models.CASCADE)
    latitud = models.FloatField(null=True, blank=True, default=None)
    longitud = models.FloatField(null=True, blank=True, default=None)
    velocidad = models.FloatField(null=True, blank=True, default=None)
    aceleracion = models.FloatField(null=True, blank=True, default=None)
    azimuth = models.FloatField(null=True, blank=True, default=None) 