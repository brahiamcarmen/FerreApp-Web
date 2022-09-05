from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from Ferre.models import Clientes, Proveedor, Productos, Ventas

class AddClientes(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"
        labels ={
            'Idcliente': _(u'Cc o Nit'),
            'Nombrecompleto': _(u'Nombre completo o razon social'),
            'Direccion': _(u'Direccion completa'),
            'Telefono': _(u'Telefono'),
            'Correo': _(u'Correo electronico'),
            'Tipocliente': _(u'Tipo de cliente'),
            'CedulaRepresentante': _(u'Cedula representante legal'),
            'NombreRepresentante': _(u'Nombre representante legal'),
            'telefonoRepresentante': _(u'telefono representante legal'),
        }

    def __init__(self, clientes=None, *args, **kwargs):
        super(AddClientes, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UpdateClientes(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"
        labels ={
            'Idcliente': _(u''),
            'Nombrecompleto': _(u'Nombre completo o razon social'),
            'Direccion': _(u'Direccion completa'),
            'Telefono': _(u'Telefono'),
            'Correo': _(u'Correo electronico'),
            'Tipocliente': _(u'Tipo de cliente'),
            'CedulaRepresentante': _(u'Cedula representante legal'),
            'NombreRepresentante': _(u'Nombre representante legal'),
            'telefonoRepresentante': _(u'telefono representante legal'),
        }
        widgets = {
            'Idcliente': forms.HiddenInput(),
        }

    def __init__(self, clientes=None, *args, **kwargs):
        super(UpdateClientes, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class AddProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"
        labels ={
            'IdProveedor': _(u'Cc o Nit'),
            'Nombrecompleto': _(u'Nombre completo o razon social'),
            'Direccion': _(u'Direccion completa'),
            'Telefono': _(u'Telefono'),
            'Correo': _(u'Correo electronico'),
            'TipoProveedor': _(u'Tipo de proveedor'),
            'ClaseProveedor': _(u'Clase de proveedor'),
            'CedulaRepresentante': _(u'Cedula representante legal'),
            'NombreRepresentante': _(u'Nombre representante legal'),
            'Rut': _(u'Registro unico tributario'),
            'cuentapago1': _(u'Cuenta de pago 1'),
            'tipocuenta1': _(u'Tipo cuenta 1'),
            'cuentapago2': _(u'Cuenta de pago 2 (opcional)'),
            'tipocuenta2': _(u'Tipo cuenta 2'),
        }

    def __init__(self, clientes=None, *args, **kwargs):
        super(AddProveedor, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UpdateProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"
        labels ={
            'IdProveedor': _(u''),
            'Nombrecompleto': _(u'Nombre completo o razon social'),
            'Direccion': _(u'Direccion completa'),
            'Telefono': _(u'Telefono'),
            'Correo': _(u'Correo electronico'),
            'TipoProveedor': _(u'Tipo de proveedor'),
            'ClaseProveedor': _(u'Clase de proveedor'),
            'CedulaRepresentante': _(u'Cedula representante legal'),
            'NombreRepresentante': _(u'Nombre representante legal'),
            'Rut': _(u'Registro unico tributario'),
            'cuentapago1': _(u'Cuenta de pago 1'),
            'tipocuenta1': _(u'Tipo cuenta 1'),
            'cuentapago2': _(u'Cuenta de pago 2 (opcional)'),
            'tipocuenta2': _(u'Tipo cuenta 2'),
        }

        widgets = {
            'IdProveedor': forms.HiddenInput(),
        }

    def __init__(self, proveedor=None, *args, **kwargs):
        super(UpdateProveedor, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class AddProductos(forms.ModelForm):
    class Meta:
        model = Productos
        fields = "__all__"
        labels ={
            'NombreProducto': _(u'Descripcion'),
            'Categoria': _(u'Categoria'),
            'Stock': _(u'Stock'),
            'PrecioVenta': _(u'Precio de Venta'),
            'Historico': _(u'Historico (valor igual al Stock)'),
        }

    def __init__(self, clientes=None, *args, **kwargs):
        super(AddProductos, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class AddStock(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'PrecioVenta'
        ]
        labels ={
            'PrecioVenta': _(u'Precio de Venta'),
        }

    def __init__(self, clientes=None, *args, **kwargs):
        super(AddStock, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class AddVenta(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = [
            'Cliente',
            'Domicilio',
        ]
        labels ={
            'Cliente': _(u'Cliente'),
            'Domicilio': _(u'Domicilio')
        }
    def __init__(self, clientes=None, *args, **kwargs):
        super(AddVenta, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})