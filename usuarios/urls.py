from django.conf.urls import url
from usuarios.views import Inicio

urlpatterns = [
    url(r'^inicio/', Inicio.as_view(), name='inicio'),
]