from django import forms
from apps.producto.models import Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto

        fields = [
            'nombre',
            'tipo',
            'descripcion',
            'precio',
            
        ]

        label = {
            'nombre' : 'Nombre',
            'tipo' : 'Tipo',
            'descripcion' : 'Descripción',
            'precio' : 'Precio',
            
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'select'}),
            'descripcion': forms.TextInput(attrs={'class':'input-field'}),
            'precio': forms.TextInput(attrs={'class':'input-field'}),
           
        }