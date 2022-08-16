from django.conf.urls import url
from usuarios.views import Inicio, ListaClientes, AgregarClientes, ListaProveedores, Agregarproveedor

urlpatterns = [
    url(r'^inicio/', Inicio.as_view(), name='inicio'),
    url(r'listadoclientes', ListaClientes.as_view(), name='listadoclientes'),
    url(r'agregarcliente', AgregarClientes.as_view(), name='agregarcliente'),
    url(r'listadoproveedores', ListaProveedores.as_view(), name='listadoproveedores'),
    url(r'agregarproveedor', Agregarproveedor.as_view(), name='agregarproveedor'),
]