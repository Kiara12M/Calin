from rest_framework import serializers
from Productos.models.pedido_models import Pedido, DetallePedido
from Productos.serializers.producto_serializer import ProductoSerializer

class DetallePedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    
    class Meta:
        model = DetallePedido
        fields = ['id', 'producto', 'cantidad', 'precio_unitario']

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pedido
        fields = ['id', 'total', 'estado', 'transaction_id', 'creado', 'detalles']
