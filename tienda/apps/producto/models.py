from django.db import models

# Create your models here.


# Modelo de tipo de producto
class TipoProducto(models.Model):
    nombreTipo = models.CharField(max_length = 50)

    # para que se muestre el nombre del tipo de producto y no su código
    # al momento de ingresar un nuevo producto

    def __str__(self):
        return '{}'.format(self.nombreTipo)


# Modelo para el producto

class Producto (models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion =models.CharField(max_length = 150)
    precio = models.CharField(max_length = 50)
    tipo = models.ForeignKey(TipoProducto, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)