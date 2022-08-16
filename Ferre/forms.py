from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from Ferre.models import Clientes

class AddClientes(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"
        labels ={
            'Idcliente': _(u'Cc o Nit'),
            'Nombrecompleto': _(u'Nombre completo o razon social'),
            'Direccion': _(u'Direccion completa'),
            'Telefono': _(u'Telefono'),
            'Tipocliente': _(u'Tipo de cliente'),
            'CedulaRepresentante': _(u'Cedula representante legal'),
            'NombreRepresentante': _(u'Nombre representante legal'),
        }

    def __init__(self, Clientes=None, *args, **kwargs):
        super(AddClientes, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})