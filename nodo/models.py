from django.db import models

class Nodo(models.Model):

    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()