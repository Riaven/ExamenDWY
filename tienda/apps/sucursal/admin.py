from django.contrib import admin
from apps.sucursal.models import Comuna, Ciudad, Sucursal
# Register your models here.


admin.site.register(Comuna)
admin.site.register(Ciudad)
admin.site.register(Sucursal)