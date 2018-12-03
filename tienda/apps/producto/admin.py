from django.contrib import admin
from apps.producto.models import TipoProducto, Producto
# Register your models here.


admin.site.register(TipoProducto)
admin.site.register(Producto)