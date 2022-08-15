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
from Ferre.models import Usuario

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
            return render(request,
                          self.template_name,{'proyecto': proyectov,'version':versionp},
                            )
        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")