from django.contrib import admin
from Productos.models.pedido_models import Pedido, DetallePedido

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'total', 'estado', 'transaction_id', 'creado')
    list_filter = ('estado', 'creado')
    search_fields = ('transaction_id', 'usuario__email')
    inlines = [DetallePedidoInline]
