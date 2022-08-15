from django.conf.urls import url
from usuarios.views import Inicio, ListaClientes

urlpatterns = [
    url(r'^inicio/', Inicio.as_view(), name='inicio'),
    url(r'listadoclientes', ListaClientes.as_view(), name='listadoclientes')
]