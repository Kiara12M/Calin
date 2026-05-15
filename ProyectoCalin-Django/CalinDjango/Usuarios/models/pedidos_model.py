from django.db import models
from django.conf import settings

class Pedidos(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("enviado", "Enviado"),
        ("entregado", "Entregado"),
        ("cancelado", "Cancelado"),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True) #desde cuando salió el pedido
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente") #no he puesto booleano porque le he creado una lista
    total = models.DecimalField(max_digits=10, decimal_places=2)
    direccion_envio = models.CharField(max_length=200)



    def __str__(self):
        return f"Pedido {self.id} - {self.usuario}"
