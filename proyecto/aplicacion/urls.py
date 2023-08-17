from django.urls import path, include 

from .views import *

urlpatterns = [
    path('', home, name= 'home' ),

    path('venta/', venta, name= 'venta' ),
    path('venta_form2/', ventaForm2, name= 'venta_form2' ),
    path('buscar_ventas/', buscarVentas, name= 'buscar_ventas' ),

    path('alquiler/', alquiler, name= 'alquiler' ),
    path('alquiler_form2/', alquilerForm2, name= 'alquiler_form2' ),
    path('buscar_alquiler/', buscarAlquiler, name= 'buscar_alquiler' ),
    
    path('asesores/', asesores, name= 'asesores' ),
    path('asesores_form2/', asesoresForm2, name= 'asesores_form2' ), 
]