from django.urls import path
from . import views

urlpatterns = [
    path('', views.measurement_list, name='Measurements'),
    path('<int:pk>/', views.measurement, name='Measurement'),
    path('log/', views.log_measurment, name='Log Measurement'),
    path('nodo/<int:nd>/', views.measurementNodo, name='MeasurementNodo')
]