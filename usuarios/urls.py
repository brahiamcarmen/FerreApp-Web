from django.conf.urls import url
from usuarios.views import Inicio, ListaClientes, AgregarClientes,ListadoVentas,ListaProveedores, ModificarClientes,Agregarproveedor
from usuarios.views import VerCliente, VerProveedor,VerVenta, ModificarProveedor,ListadoDomicilios, ListaProductos, AgregarProducto,AgregarStock, AgregarVenta
from usuarios.views import ActualizarDomicilio

urlpatterns = [
    url(r'^inicio/', Inicio.as_view(), name='inicio'),
    url(r'listadoclientes', ListaClientes.as_view(), name='listadoclientes'),
    url(r'agregarcliente', AgregarClientes.as_view(), name='agregarcliente'),
    url(r'listadoproveedores', ListaProveedores.as_view(), name='listadoproveedores'),
    url(r'agregarproveedor', Agregarproveedor.as_view(), name='agregarproveedor'),
    url(r'vercliente/(?P<Idcliente>\w+)', VerCliente.as_view(), name='vercliente'),
    url(r'verproveedor/(?P<Idproveedor>\w+)', VerProveedor.as_view(), name='verproveedor'),
    url(r'modificarcliente/(?P<identificador>\w+)', ModificarClientes.as_view(), name='modificarcliente'),
    url(r'modificarproveedor/(?P<identificador>\w+)', ModificarProveedor.as_view(), name='modificarproveedor'),
    url(r'listadoproductos', ListaProductos.as_view(), name='listadoproductos'),
    url(r'agregarproducto', AgregarProducto.as_view(), name='agregarproducto'),
    url(r'agregarstock/(?P<identificador>\w+)', AgregarStock.as_view(), name='agregarstock'),
    url(r'agregarventa', AgregarVenta.as_view(), name='agregarventa'),
    url(r'listadoventas/', ListadoVentas.as_view(), name='listadoventas'),
    url(r'listadodomicilios/', ListadoDomicilios.as_view(), name='listadodomicilios'),
    url(r'verventa/(?P<idventa>\w+)', VerVenta.as_view(), name='verventa'),
    url(r'actualizardomi/(?P<identificador>\w+)', ActualizarDomicilio.as_view(), name='actualizardomi'),

]