from django.urls import path
from . import views

urlpatterns = [
    path('', views.node_list, name='Nodos'),
    path('<int:pk>/', views.nodo, name='Nodo'),
    path('reg/', views.registrar_nodo, name='Registrar nodo')
]
