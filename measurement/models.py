from django.db import models
from nodo.models import Nodo

class Measurement(models.Model):

    nodo = models.ForeignKey(Nodo, on_delete=models.CASCADE)
    latitud = models.BigIntegerField(null=True, blank=True, default=None)
    longitud = models.BigIntegerField(null=True, blank=True, default=None)
    velocidad = models.FloatField(null=True, blank=True, default=None)
    aceleracion = models.FloatField(null=True, blank=True, default=None)
    azimuth = models.FloatField(null=True, blank=True, default=None) 
    positionDOP = models.PositiveIntegerField(null=True, blank=True, default=None)
    weekTime = models.BigIntegerField(null=True, blank=True, default=None)
    positionAccuracy = models.PositiveBigIntegerField(null=True, blank=True, default=None)