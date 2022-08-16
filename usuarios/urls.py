from django.conf.urls import url
from usuarios.views import Inicio, ListaClientes, AgregarClientes

urlpatterns = [
    url(r'^inicio/', Inicio.as_view(), name='inicio'),
    url(r'listadoclientes', ListaClientes.as_view(), name='listadoclientes'),
    url(r'agregarcliente', AgregarClientes.as_view(), name='agregarcliente')
]