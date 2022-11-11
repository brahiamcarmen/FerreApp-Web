import os
import socket
from django.shortcuts import render
from django.conf import settings
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.contrib import auth
from Ferre.models import Usuario, Clientes, Proveedor, Productos, Ventas, Domicilio, RegistroVentas
from Ferre.forms import AddClientes, AddProveedor, UpdateClientes, UpdateProveedor, AddProductos, AddStock, AddVcliente,UpdateDomicilio

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
            stock = Productos.objects.all()
            domicilios = Domicilio.objects.filter(Estado='Pendiente')
            contdomi = Domicilio.objects.filter(Estado='Pendiente').count()
            ventas = Ventas.objects.all().order_by('-IdVentas')[:10]
            fechaexp = (datetime.today())
            dia = fechaexp.day
            ciclo = fechaexp.month
            ano1 = fechaexp.year
            # Los argumentos serán: Año, Mes, Día, Hora, Minutos, Segundos, Milisegundos.
            new_date = datetime(ano1, ciclo, dia, 1, 00, 00, 00000)
            new_date2 = datetime(ano1, ciclo, dia, 23, 59, 59, 00000)
            cventas = Ventas.objects.filter(Fecha__gte=new_date, Fecha__lte=new_date2).all()

            contar = 0
            for i in cventas:
                if i.pk >= 1:
                    contar += 1

            valorventas = 0
            for i in cventas:
                    valorventas += i.Valor

            cantstock = 0
            for i in stock:
                cantstock += i.Stock

            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,'domi':domicilios, 'cantstock':cantstock,'stock': stock,
                                              'ventas': ventas,'contar':contar, 'valorventas':valorventas,'contdomi':contdomi}
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
                return HttpResponseRedirect(reverse('usuarios:listadoclientes'))

            else:
                messages.add_message(request, messages.ERROR, 'No se puedo agregar la informacion del cliente')
                return HttpResponseRedirect(reverse('usuarios:agregarcliente'))

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

class ListaProductos(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/listadoproductos.html'

    def get(self, request):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()

            datos = Usuario.objects.get(usuid=request.user.pk)
            productos = Productos.objects.all()
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,'productos':productos}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")


class AgregarProducto(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/agregarproducto.html'
    form = AddProductos

    def get(self, request):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            datos = Usuario.objects.get(usuid=request.user.pk)
            form = self.form
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,'formularioproductos':form,}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        try:
            datos = Usuario.objects.get(usuid=request.user.pk)
            form = self.form(request.user, request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El producto se agrego correctamente')
                return HttpResponseRedirect(reverse('usuarios:listadoproductos'))

            else:
                messages.add_message(request, messages.ERROR, 'No se pudo agregar el producto')
                return HttpResponseRedirect(reverse('usuarios:listadoproductos'))

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

class AgregarStock(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/agregarstock.html'
    form = AddStock

    def get(self, request,identificador):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()

            datos = Usuario.objects.get(usuid=request.user.pk)
            producto = Productos.objects.get(IdProducto=identificador)

            form = self.form(instance=producto)
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,'formulariostock':form,'fecha': producto.Fecha,
                                              'idproducto': producto.IdProducto, 'nombrep': producto.NombreProducto,'categoria': producto.Categoria,'historico':producto.Historico,
                                              'stock': producto.Stock, 'pventa': producto.PrecioVenta}
                            )
        except Productos.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request, identificador):
        try:
            cantidad = request.POST.get("Cantidad")
            precioventa = request.POST.get("PrecioVenta")
            producto = Productos.objects.filter(IdProducto=identificador).exists()

            datos = Usuario.objects.get(usuid=request.user.pk)

            if producto is True:
                if cantidad and precioventa is not None:
                    producto = Productos.objects.get(IdProducto=identificador)
                    suma = producto.Stock + int(cantidad)
                    producto.Stock = int(suma)
                    producto.PrecioVenta = int(precioventa)
                    historico = producto.Historico + int(cantidad)
                    producto.Historico = int(historico)
                    producto.save()
                    messages.add_message(request, messages.INFO, 'la informacion del cliente se modifico correctamente')
                    return HttpResponseRedirect(reverse('usuarios:inicio'))

                else:
                    messages.add_message(request, messages.ERROR, 'No se puedo agregar informacion al stock')
                    return HttpResponseRedirect(reverse('usuarios:inicio'))

            else:
                messages.add_message(request, messages.ERROR, 'No se puedo modificar la informacion del cliente')
                return HttpResponseRedirect(reverse('usuarios:inicio'))

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

class ListadoVentas(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/listadoventas.html'

    def get(self, request):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            datos = Usuario.objects.get(usuid=request.user.pk)
            ventas = Ventas.objects.all().order_by('-IdVentas')
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp, 'clientes': ventas}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

class AgregarVenta(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/agregarventa.html'
    form = AddVcliente

    def get(self, request):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            formulariocliente = self.form()
            if request.is_ajax():
                datos = serializers.serialize("json", Productos.objects.all())
                return HttpResponse(datos, content_type='application/json')

            else:
                return render(request,self.template_name,{'proyecto': proyectov,'version':versionp, 'form': formulariocliente})

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        try:
            usuario = Usuario.objects.get(usuid=request.user.pk)
            #bloqueinfocliente
            domicilio = request.POST.get("domicilio")
            direccion = request.POST.get("direccion")
            cedulacliente = request.POST.get("cedulacliente")
            contacto = request.POST.get("contacto")
            #bloque1
            codigo1 = request.POST.get("codigo")
            cantidad1 = request.POST.get("cant1")
            #bloque2
            codigo2 = request.POST.get("codigo2")
            cantidad2 = request.POST.get("cant2")
            #bloque3
            codigo3 = request.POST.get("codigo3")
            cantidad3 = request.POST.get("cant3")
            #bloque4
            codigo4 = request.POST.get("codigo4")
            cantidad4 = request.POST.get("cant4")
            # bloque5
            codigo5 = request.POST.get("codigo5")
            cantidad5 = request.POST.get("cant5")
            cliente = Clientes.objects.filter(Idcliente=cedulacliente).exists()
            lista = [codigo1, codigo2, codigo3, codigo4, codigo5]

            cont = 0
            for i in lista:
                if i != '':
                    cont += 1

            if cont == 1:
                producto = Productos.objects.get(IdProducto=codigo1)
                valorproducto = producto.PrecioVenta
                valorxcant = int(cantidad1) * int(valorproducto)
                cedula = Clientes.objects.get(Idcliente=cedulacliente)
                venta = Ventas(Valor=valorxcant, Cantidad=cantidad1, Cliente=cedula, Vendedor=usuario, Domicilio=domicilio)
                venta.save()
                registroventas = RegistroVentas(IdVenta=venta, IdProducto=producto,Cantidad=cantidad1, ValorUni=valorproducto, ValorTotal=valorxcant)
                registroventas.save()
                if domicilio == 'Si':
                    adddomicilio = Domicilio(IdVenta=venta, Estado='Pendiente', Direccion=direccion, Contacto=contacto)
                    adddomicilio.save()

                messages.add_message(request, messages.INFO, 'Se lee la info')
                return HttpResponseRedirect(reverse('usuarios:agregarventa'))

            elif cont ==2:
                producto1 = Productos.objects.get(IdProducto=codigo1)
                producto2 = Productos.objects.get(IdProducto=codigo2)
                print(producto1,producto2)
                messages.add_message(request, messages.INFO, 'Se lee la info')
                return HttpResponseRedirect(reverse('usuarios:agregarventa'))

            else:
                messages.add_message(request, messages.INFO, 'Error 2')
                return HttpResponseRedirect(reverse('usuarios:agregarventa'))

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

class ListadoDomicilios(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/listadodomicilios.html'

    def get(self, request):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            datos = Usuario.objects.get(usuid=request.user.pk)
            domicilios = Domicilio.objects.all()
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp, 'domicilios': domicilios}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

class VerVenta(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/verventa.html'

    def get(self, request, idventa):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()

            venta = Ventas.objects.get(IdVentas=idventa)
            noventa = venta.IdVentas
            fecha = venta.Fecha
            valor = venta.Valor
            cantidad = venta.Cantidad
            domicilio = venta.Domicilio
            nombrev = venta.Vendedor.usuid.first_name
            apellidov = venta.Vendedor.usuid.last_name
            nombrevendedor = nombrev + ' ' + apellidov
            idcliente = venta.Cliente.pk
            cliente = Clientes.objects.get(Idcliente=idcliente)
            nombrecliente = cliente.Nombrecompleto
            registroventas = RegistroVentas.objects.filter(IdVenta=idventa)
            otdomicilio = Domicilio.objects.filter(IdVenta=idventa)
            return render(request,self.template_name,{'proyecto': proyectov,'version':versionp,'domicilio': domicilio,'vendedor':nombrevendedor,
                                                          'cantidad': cantidad, 'valor': valor, 'noventa': noventa, 'fecha': fecha,
                                                      'registroventas': registroventas,'cedula': idcliente, 'nombrecliente': nombrecliente,'domicilios': otdomicilio})

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

class ActualizarDomicilio(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'usuarios/actualizardomi.html'
    form = UpdateDomicilio

    def get(self, request, identificador):
        try:
            nombre = open('static/serial/NombreProyecto.txt', 'r')
            proyectov = nombre.read()
            version = open('static/serial/Version.txt', 'r')
            versionp = version.read()
            iddomicilio = identificador
            domicilio = Domicilio.objects.get(IdDomicilio=iddomicilio)
            Direccion = domicilio.Direccion
            datos = Usuario.objects.get(usuid=request.user.pk)

            form = self.form(instance=domicilio)
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp,'formulario':form,
                                              'identificador': iddomicilio, 'direccion': Direccion}
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")
