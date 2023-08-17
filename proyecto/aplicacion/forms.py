from django import forms

class AlquilerForm(forms.Form):
    tipo= forms.CharField(max_length=50, required= True)
    ambientes= forms.IntegerField(required=True)
    localidad = forms.CharField(max_length=50,required= True)
    precio= forms.IntegerField(required=True)


class VentaForm(forms.Form):
    tipo= forms.CharField(max_length=50, required= True)
    ambientes= forms.IntegerField(required=True)
    localidad = forms.CharField(max_length=50,required= True)
    precio= forms.IntegerField(required=True)




class AsesoresForm(forms.Form):
    nombre= forms.CharField(max_length=50, required= True)
    apellido= forms.CharField(max_length=50,required=True)
    telefono = forms.IntegerField(required= True)
    email= forms.EmailField(required=True)

