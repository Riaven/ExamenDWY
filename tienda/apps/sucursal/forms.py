from django import forms
from apps.sucursal.models import Sucursal

class SucursalForm(forms.ModelForm):
    
    class Meta:
        model = Sucursal

        fields = [
            'nombreTienda',
            'direccion',
            'telefono',
            'correo',
            'encargado',
            'comuna' ,
            'ciudad' ,
            
        ]

        label = {
            'nombreTienda' : 'Nombre de tienda',
            'direccion' : 'Dirección',
            'telefono' : 'Teléfono',
            'correo' : 'Correo Electrónico',
            'encargado' : 'Encargado de Local',
            'comuna' : 'Comuna',
            'ciudad' : 'Ciudad',
            
        }

        widgets = {

            'nombreTienda' : forms.TextInput(attrs={'class':'form-control'}),,
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),,
            'telefono' : forms.TextInput(attrs={'class':'form-control'}),,
            'correo' : forms.TextInput(attrs={'class':'form-control'}),,
            'encargado' :forms.TextInput(attrs={'class':'form-control'}), ,
            'comuna' : forms.Select(attrs={'class':'select'}),,
            'ciudad' : forms.Select(attrs={'class':'select'}),,
            
           
        }