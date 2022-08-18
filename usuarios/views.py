import os
import socket
from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
import speedtest
from django.contrib import auth
from Ferre.models import Usuario, Clientes, Proveedor
from Ferre.forms import AddClientes, AddProveedor, UpdateClientes, UpdateProveedor

class Inicio(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/inicio.html'

    def get(self, request):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            datos = Usuario.objects.get(usuid=request.user.pk)
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp},
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

class ListaClientes(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/listadoclientes.html'

    def get(self, request):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            datos = Usuario.objects.get(usuid=request.user.pk)
            clientes = Clientes.objects.all()
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,'clientes':clientes}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

class AgregarClientes(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/agregarcliente.html'
    form = AddClientes

    def get(self, request):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            datos = Usuario.objects.get(usuid=request.user.pk)
            form = self.form
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,'formulariocliente':form,}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        try:
            datos = Usuario.objects.get(usuid=request.user.pk)
            form = self.form(request.user, request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'la informacion del cliente se agrego correctamente')
                return HttpResponseRedirect(reverse('usuarios:inicio'))

            else:
                messages.add_message(request, messages.ERROR, 'No se puedo agregar la informacion del cliente')
                return HttpResponseRedirect(reverse('usuarios:inicio'))

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")


class ModificarClientes(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/modificarcliente.html'
    form = UpdateClientes

    def get(self, request, identificador):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            IdCliente = identificador
            datos = Usuario.objects.get(usuid=request.user.pk)
            datoscliente = Clientes.objects.get(Idcliente=IdCliente)
            form = self.form(instance=datoscliente)
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,'formulariocliente':form,}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request, identificador):
        try:
            IdCliente = identificador
            datos = Usuario.objects.get(usuid=request.user.pk)
            datoscliente = Clientes.objects.get(Idcliente=IdCliente)
            form = self.form(request.user, request.POST, instance=datoscliente)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'la informacion del cliente se modifico correctamente')
                return HttpResponseRedirect(reverse('usuarios:inicio'))

            else:
                messages.add_message(request, messages.ERROR, 'No se puedo modificar la informacion del cliente')
                return HttpResponseRedirect(reverse('usuarios:inicio'))

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")


class ListaProveedores(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/listadoproveedores.html'

    def get(self, request):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            datos = Usuario.objects.get(usuid=request.user.pk)
            proveedores = Proveedor.objects.all()
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,'proveedores':proveedores}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")


class Agregarproveedor(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/agregarproveedor.html'
    form = AddProveedor

    def get(self, request):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            datos = Usuario.objects.get(usuid=request.user.pk)
            form = self.form
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,'formularioproveedor':form,}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        try:
            datos = Usuario.objects.get(usuid=request.user.pk)
            form = self.form(request.user, request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'la informacion del proveedor se agrego correctamente')
                return HttpResponseRedirect(reverse('usuarios:inicio'))

            else:
                messages.add_message(request, messages.ERROR, 'No se puedo agregar la informacion del proveedor')
                return HttpResponseRedirect(reverse('usuarios:inicio'))

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")


class VerCliente(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/verinfocliente.html'

    def get(self, request, Idcliente):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            datos = Usuario.objects.get(usuid=request.user.pk)
            cliente = Clientes.objects.get(Idcliente=Idcliente)
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,
                                              'identificador': cliente.Idcliente,
                                              'nombre': cliente.Nombrecompleto,
                                              'direccion':cliente.Direccion,
                                              'correo': cliente.Correo,
                                              'telefono': cliente.Telefono,
                                              'tipo': cliente.Tipocliente,
                                              'nombrer': cliente.NombreRepresentante,
                                              'identir':cliente.CedulaRepresentante,
                                              'telefonor':cliente.telefonoRepresentante}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")


class VerProveedor(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/verproveedor.html'

    def get(self, request, Idproveedor):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            datos = Usuario.objects.get(usuid=request.user.pk)
            cliente = Proveedor.objects.get(IdProveedor=Idproveedor)
            return render(request,self.template_name,{'proyecto': proyectov,'version':versionp,
                                              'identificador': cliente.IdProveedor,
                                              'nombre': cliente.Nombrecompleto,
                                              'direccion':cliente.Direccion,
                                              'correo': cliente.Correo,
                                              'telefono': cliente.Telefono,
                                              'tipo': cliente.TipoProveedor,
                                              'clase':cliente.ClaseProveedor,
                                              'nombrer': cliente.NombreRepresentante,
                                              'identir':cliente.CedulaRepresentante,
                                              'telefonor':cliente.TelefonoRepresentante,
                                              'rut': cliente.Rut,
                                              'tipo1': cliente.tipocuenta1,
                                              'tipo2': cliente.tipocuenta2,
                                              'cuenta1': cliente.cuentapago1,
                                              'cuenta2': cliente.cuentapago2}
                            )
        except Proveedor.DoesNotExist:
            return render(request, "pages-404.html")

class ModificarProveedor(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/modificarproveedor.html'
    form = UpdateProveedor

    def get(self, request, identificador):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            IdProveedor= identificador
            datos = Usuario.objects.get(usuid=request.user.pk)
            datosproveedor = Proveedor.objects.get(IdProveedor=IdProveedor)
            form = self.form(instance=datosproveedor)
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,'identificador': IdProveedor,'formularioproveedor':form,}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request, identificador):
        try:
            IdProveedor= identificador
            datos = Usuario.objects.get(usuid=request.user.pk)
            datosproveedor = Proveedor.objects.get(IdProveedor=IdProveedor)
            form = self.form(request.user, request.POST, instance=datosproveedor)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'la informacion del cliente se modifico correctamente')
                return HttpResponseRedirect(reverse('usuarios:inicio'))

            else:
                messages.add_message(request, messages.ERROR, 'No se puedo modificar la informacion del cliente')
                return HttpResponseRedirect(reverse('usuarios:inicio'))

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")