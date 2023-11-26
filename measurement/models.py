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
    timestamp = models.DateTimeField(null=True, blank=True, default=None)
    
    def save(self, *args, **kwargs):
        if self.timestamp_components_valid():
            self.timestamp = self._create_timestamp()
        super().save(*args, **kwargs)
    
    def timestamp_components_valid(self):
        return all(
            getattr(self, component) is not None
            for component in ['year', 'month', 'day', 'hour', 'minute', 'second']
        )

    def _create_timestamp(self):
        from datetime import datetime
        return datetime(
            year=self.year,
            month=self.month,
            day=self.day,
            hour=self.hour,
            minute=self.minute,
            second=self.second,
        )