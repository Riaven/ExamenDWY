from django.db import models

# Create your models here.
# modelo de comuna
class Comuna (models.Model):
    nombreComuna = models.CharField(max_length = 50)

    # para que retorne el nombre de la comuna
    def __str__(self):
        return '{}'.format(self.nombreComuna)

class Ciudad (models.Model):
    nombreCiudad = models.CharField(max_length = 50)
    comuna = models.ForeignKey(Comuna, default=1, on_delete=models.CASCADE)


    # para que retorne el nombre de la comuna
    def __str__(self):
        return '{}'.format(self.nombreCiudad)


class Sucursal (models.Model):
    nombreTienda = models.CharField(max_length = 50) 
    direccion = models.CharField(max_length = 150) 
    telefono = models.CharField(max_length = 10) 
    correo = models.CharField(max_length = 50) 
    encargado = models.CharField(max_length = 50) 
    comuna = models.ForeignKey(Comuna, default=1, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, default=1, on_delete=models.CASCADE)


    # para que retorne el nombre de la comuna
    def __str__(self):
        return '{}'.format(self.nombreCiudad)