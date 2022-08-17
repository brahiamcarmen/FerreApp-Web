#-*-coding:utf-8-*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

DOC_CHOICES2 = (
    ('Administrador', _(u"Administrador")),
    ('Auxiliar', _(u"Auxiliar")),
)

class Usuario(models.Model):
    IdUsuario = models.AutoField(primary_key=True)
    FotoUsuario = models.ImageField(upload_to='usuarios', default='usuarios/usuario.png')
    TipoUsuario = models.CharField(max_length=100, blank=True, null=True, choices=DOC_CHOICES2, default='Auxiliar')
    FechaCreacion = models.DateTimeField(auto_now_add=True)
    celular = models.CharField(max_length=10, null=False)
    usuid = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.usuid.username)

    class Meta:
        verbose_name_plural = "Datos usuarios"
        verbose_name = "Datos usuario"

DOC_CHOICES = (
    ('Persona natural', _(u"Persona natural")),
    ('Personeria juridica', _(u"Pesoneria juridica")),
)

class Clientes(models.Model):
    Idcliente = models.CharField(primary_key=True, max_length=25, null=False)
    Nombrecompleto = models.CharField(max_length=100, null=False)
    Direccion = models.CharField(max_length=50, null=False)
    Telefono = models.CharField(max_length=50, null=False)
    Correo = models.EmailField(max_length=50, null=True)
    Tipocliente = models.CharField(max_length= 50, null=False, choices=DOC_CHOICES)
    CedulaRepresentante = models.CharField(max_length=50, null=True)
    NombreRepresentante = models.CharField(max_length=50, null=True)
    telefonoRepresentante = models.IntegerField(null=True)

    def __str__(self):
        return "%s %s" % (self.Idcliente, self.Nombrecompleto)

    class Meta:
        verbose_name_plural = "Datos clientes"
        verbose_name = "Datos cliente"

DOC_CHOICES1 = (
    ('Minoristas', _(u"Minorista")),
    ('Mayorista', _(u"Mayorista")),
)

DOC_CHOICES3 = (
    ('Cuenta de ahorro', _(u"Cuenta de ahorro")),
    ('Cuenta corriente', _(u"Cuenta corriente")),
)
class Proveedor(models.Model):
    IdProveedor = models.CharField(primary_key=True, max_length=25, null=False)
    Nombrecompleto = models.CharField(max_length=100, null=False)
    Direccion = models.CharField(max_length=50, null=False)
    Telefono = models.CharField(max_length=50, null=False)
    Correo = models.EmailField(max_length=50, null=True)
    TipoProveedor = models.CharField(max_length= 50, null=False, choices=DOC_CHOICES)
    ClaseProveedor = models.CharField(max_length= 50, null=False, choices=DOC_CHOICES1)
    CedulaRepresentante = models.CharField(max_length=50, null=True)
    NombreRepresentante = models.CharField(max_length=50, null=True)
    TelefonoRepresentante = models.CharField(max_length=10, null=True)
    Rut = models.IntegerField(null=True)
    cuentapago1 = models.CharField(max_length=50, null=True)
    tipocuenta1 = models.CharField(max_length= 35, null=True, choices=DOC_CHOICES3)
    cuentapago2 = models.CharField(max_length=50, null=True)
    tipocuenta2 = models.CharField(max_length=35, null=True, choices=DOC_CHOICES3)


    def __str__(self):
        return "%s %s" % (self.IdProveedor, self.Nombrecompleto)

    class Meta:
        verbose_name_plural = "Datos proveedor"
        verbose_name = "Datos proveedor"

class Productos(models.Model):
    IdProducto = models.CharField(primary_key=True, max_length=25, null=False)
    NombreProducto = models.CharField(max_length=100, null=False)
    Categoria = models.CharField(max_length=100, null=False)
    Proveedor = models.CharField(max_length=50, null=False)
    Stock = models.IntegerField(null=True)
    precioUnidad = models.IntegerField(null=True)
    Historico = models.IntegerField(null=True)

    def __str__(self):
        return "%s %s" % (self.IdProducto, self.NombreProducto)

    class Meta:
        verbose_name_plural = "Datos productos"
        verbose_name = "Dato producto"