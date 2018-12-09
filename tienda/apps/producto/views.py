from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.producto.forms import ProductoForm
from apps.producto.models import Producto
from django.contrib.auth.decorators import login_required

# Create your views here.


# view para el index de la página
def index(request):
    return render (request, 'principal/index.html')