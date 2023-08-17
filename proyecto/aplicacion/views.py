from django.shortcuts import render   
from django.http import HttpResponse
from .models import Alquileres, Venta , Asesores
from .forms import AlquilerForm, VentaForm, AsesoresForm

def home(request):
    return render (request, 'aplicacion/home.html') 

def alquiler(request):
    contexto= {'alquileres': Alquileres.objects.all() } 
    return render (request, 'aplicacion/alquiler.html', contexto) 

def venta(request):
    contexto= {'ventas': Venta.objects.all()}
    return render (request, 'aplicacion/venta.html',contexto)

def asesores(request):
    contexto = {'asesores': Asesores.objects.all()}
    return render (request,'aplicacion/asesores.html',contexto)


# Formulario de Alquileres vinculado a la clase del FORMS

def alquilerForm2(request):
    if request.method == "POST":
       miForm = AlquilerForm(request.POST)
       if miForm.is_valid():
           alquiler_tipo = miForm.cleaned_data.get ('tipo')
           alquiler_ambientes = miForm.cleaned_data.get ('ambientes')
           alquiler_localidad = miForm.cleaned_data.get ('localidad')
           alquiler_precio = miForm.cleaned_data.get ('precio')
           alquiler= Alquileres(tipo=alquiler_tipo,
                             ambientes= alquiler_ambientes,
                             localidad= alquiler_localidad,
                             precio= alquiler_precio )
           alquiler.save()
           return render(request,"aplicacion/base.html")     
    else:
       miForm = AlquilerForm()
    return render(request, "aplicacion/alquilerForm2.html" , {"form": miForm})


# Formulario de Ventas vinculado a la clase del FORMS

def ventaForm2(request):
    if request.method == "POST":
       miForm = VentaForm(request.POST)
       if miForm.is_valid():
           venta_tipo = miForm.cleaned_data.get ('tipo')
           venta_ambientes = miForm.cleaned_data.get ('ambientes') 
           venta_localidad = miForm.cleaned_data.get ('localidad')
           venta_precio = miForm.cleaned_data.get ('precio')
           venta_financiamiento = miForm.cleaned_data.get ('financiamiento')
           venta= Venta(tipo=venta_tipo,
                             ambientes= venta_ambientes,
                             localidad= venta_localidad ,
                             precio= venta_precio,
                             financiamiento = venta_financiamiento )
           venta.save()
           return render(request,"aplicacion/base.html")     
    else:
       miForm = VentaForm()
    return render(request, "aplicacion/ventaForm2.html" , {"form": miForm})


# Formulario de Asesores vinculado a la clase del FORMS

def asesoresForm2(request):
    if request.method == "POST":
       miForm = AsesoresForm(request.POST)
       if miForm.is_valid():
           asesor_nombre = miForm.cleaned_data.get ('nombre')
           asesor_apellido = miForm.cleaned_data.get ('apellido')
           asesor_telefono = miForm.cleaned_data.get ('telefono')
           asesor_email = miForm.cleaned_data.get ('email')
           asesor = Asesores(nombre = asesor_nombre,
                             apellido= asesor_apellido,
                             telefono= asesor_telefono ,
                             email= asesor_email )
           asesor.save()
           return render(request,"aplicacion/base.html")     
    else:
       miForm = AsesoresForm()
    return render(request, "aplicacion/asesoresForm2.html" , {"form": miForm})

# Buscadores 

def buscarAlquiler(request):
    if request.GET ['buscar']:
        patron = request.GET['buscar']
        alquileres= Alquileres.objects.filter(tipo__icontains=patron)
        contexto = {'alquileres': alquileres }                             
        return render (request, 'aplicacion/buscar.html', contexto)
    return HttpResponse('No se ingreso nada a buscar')

def buscarVentas(request):
    if request.GET ['buscar']:
        patron = request.GET['buscar']
        ventas= Venta.objects.filter(tipo__icontains=patron)
        contexto = {'ventas':ventas }                             
        return render (request, 'aplicacion/buscar.html', contexto)
    return HttpResponse('No se ingreso nada a buscar')

 