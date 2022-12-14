# Generated by Django 3.1.3 on 2022-09-10 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('Idcliente', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Nombrecompleto', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=50, null=True)),
                ('Telefono', models.CharField(max_length=50, null=True)),
                ('Correo', models.EmailField(max_length=50, null=True)),
                ('Tipocliente', models.CharField(choices=[('Persona natural', 'Persona natural'), ('Personeria juridica', 'Pesoneria juridica')], max_length=50)),
                ('CedulaRepresentante', models.CharField(max_length=50, null=True)),
                ('NombreRepresentante', models.CharField(max_length=50, null=True)),
                ('telefonoRepresentante', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Datos cliente',
                'verbose_name_plural': 'Datos clientes',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('IdProducto', models.AutoField(primary_key=True, serialize=False)),
                ('NombreProducto', models.CharField(max_length=100)),
                ('Categoria', models.CharField(max_length=100)),
                ('Stock', models.IntegerField(null=True)),
                ('PrecioVenta', models.IntegerField(null=True)),
                ('Historico', models.IntegerField(null=True)),
                ('Fecha', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Dato producto',
                'verbose_name_plural': 'Datos productos',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('IdProveedor', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Nombrecompleto', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('Correo', models.EmailField(max_length=50, null=True)),
                ('TipoProveedor', models.CharField(choices=[('Persona natural', 'Persona natural'), ('Personeria juridica', 'Pesoneria juridica')], max_length=50)),
                ('ClaseProveedor', models.CharField(choices=[('Minoristas', 'Minorista'), ('Mayorista', 'Mayorista')], max_length=50)),
                ('CedulaRepresentante', models.CharField(max_length=50, null=True)),
                ('NombreRepresentante', models.CharField(max_length=50, null=True)),
                ('TelefonoRepresentante', models.CharField(max_length=10, null=True)),
                ('Rut', models.IntegerField(null=True)),
                ('cuentapago1', models.CharField(max_length=50, null=True)),
                ('tipocuenta1', models.CharField(choices=[('Cuenta de ahorro', 'Cuenta de ahorro'), ('Cuenta corriente', 'Cuenta corriente')], max_length=35, null=True)),
                ('cuentapago2', models.CharField(max_length=50, null=True)),
                ('tipocuenta2', models.CharField(choices=[('Cuenta de ahorro', 'Cuenta de ahorro'), ('Cuenta corriente', 'Cuenta corriente')], max_length=35, null=True)),
            ],
            options={
                'verbose_name': 'Datos proveedor',
                'verbose_name_plural': 'Datos proveedor',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('IdUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('FotoUsuario', models.ImageField(default='usuarios/usuario.png', upload_to='usuarios')),
                ('TipoUsuario', models.CharField(blank=True, choices=[('Administrador', 'Administrador'), ('Auxiliar', 'Auxiliar')], default='Auxiliar', max_length=100, null=True)),
                ('FechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('celular', models.CharField(max_length=10)),
                ('usuid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Datos usuario',
                'verbose_name_plural': 'Datos usuarios',
            },
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('IdVentas', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha', models.DateTimeField(auto_now=True)),
                ('Valor', models.IntegerField(null=True)),
                ('Cantidad', models.IntegerField(null=True)),
                ('Domicilio', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=5)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ferre.clientes')),
                ('Vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ferre.usuario')),
            ],
            options={
                'verbose_name': 'Dato venta',
                'verbose_name_plural': 'Datos ventas',
                'ordering': ['Fecha'],
            },
        ),
        migrations.CreateModel(
            name='RegistroVentas',
            fields=[
                ('IdRegistroVenta', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad', models.CharField(max_length=100, null=True)),
                ('ValorUni', models.CharField(max_length=100, null=True)),
                ('ValorTotal', models.CharField(max_length=100, null=True)),
                ('IdProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ferre.productos')),
                ('IdVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ferre.ventas')),
            ],
            options={
                'verbose_name': 'Registro Venta',
                'verbose_name_plural': 'Registro Ventas',
            },
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('IdDomicilio', models.AutoField(primary_key=True, serialize=False)),
                ('Estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Entregado', 'Entregado')], max_length=15)),
                ('Direccion', models.CharField(max_length=60)),
                ('Contacto', models.CharField(max_length=60)),
                ('FechaEntrega', models.DateTimeField(auto_now=True)),
                ('IdVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ferre.ventas')),
            ],
            options={
                'verbose_name': 'Dato domicilio',
                'verbose_name_plural': 'Datos domicilios',
                'ordering': ['FechaEntrega'],
            },
        ),
    ]
