from django.db import models
from django.conf import settings
from .producto_models import Producto

class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Usuario")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total del Pedido")
    estado = models.CharField(max_length=50, default="Pagado con PayPal", verbose_name="Estado")
    transaction_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID de Transacción PayPal")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        db_table = 'pedidos'
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-creado']

    def __str__(self):
        return f"Pedido #{self.id} - {self.total}€"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE, verbose_name="Pedido")
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, verbose_name="Producto")
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")

    class Meta:
        db_table = 'detalle_pedidos'
        verbose_name = "Detalle de Pedido"
        verbose_name_plural = "Detalles de Pedido"

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre if self.producto else 'Eliminado'}"
