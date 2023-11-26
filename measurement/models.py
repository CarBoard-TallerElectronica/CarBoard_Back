from django.db import models
from nodo.models import Nodo

class Time(models.Model):
    year = models.PositiveIntegerField(null=True, blank=True, default=None)
    month = models.PositiveIntegerField(null=True, blank=True, default=None)
    day = models.PositiveIntegerField(null=True, blank=True, default=None)
    hour = models.PositiveIntegerField(null=True, blank=True, default=None)
    minute = models.PositiveIntegerField(null=True, blank=True, default=None)
    second = models.PositiveIntegerField(null=True, blank=True, default=None)


class Measurement(models.Model):
    nodo = models.ForeignKey(Nodo, on_delete=models.CASCADE)
    latitud = models.BigIntegerField(null=True, blank=True, default=None)
    longitud = models.BigIntegerField(null=True, blank=True, default=None)
    velocidad = models.FloatField(null=True, blank=True, default=None)
    aceleracion = models.FloatField(null=True, blank=True, default=None)
    azimuth = models.FloatField(null=True, blank=True, default=None) 
    positionDOP = models.PositiveIntegerField(null=True, blank=True, default=None)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, null=True, blank=True, default=None)
    
