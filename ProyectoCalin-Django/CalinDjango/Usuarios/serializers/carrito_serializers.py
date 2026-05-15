from rest_framework import serializers
from Usuarios.models.carrito_model import Carrito, ItemCarrito
from Productos.serializers import ProductoSerializer

class ItemCarritoSerializer(serializers.ModelSerializer):
    producto_detalle = ProductoSerializer(source='producto', read_only=True)

    class Meta:
        model = ItemCarrito
        fields = ['id', 'producto', 'producto_detalle', 'cantidad', 'subtotal']
        read_only_fields = ['subtotal']

class CarritoSerializer(serializers.ModelSerializer):
    items = ItemCarritoSerializer(many=True, read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Carrito
        fields = ['id', 'usuario', 'creado', 'actualizado', 'items', 'total']
        read_only_fields = ['usuario']
