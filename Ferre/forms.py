from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from Ferre.models import Clientes, Proveedor

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
        }

    def __init__(self, clientes=None, *args, **kwargs):
        super(AddClientes, self).__init__(*args, **kwargs)

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
        }

    def __init__(self, clientes=None, *args, **kwargs):
        super(AddProveedor, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})