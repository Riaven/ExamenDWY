from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.producto.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]