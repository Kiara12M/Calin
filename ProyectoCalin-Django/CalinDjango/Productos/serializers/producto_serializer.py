from rest_framework import serializers
from Productos.models import Producto, Categoria


class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    description = serializers.CharField(source='descripcion', required=False, allow_blank=True, allow_null=True)
    precio = serializers.DecimalField(required=True, decimal_places=2, max_digits=10)
    imagen = serializers.ImageField(required=False, allow_null=True)
    categoria = serializers.CharField(required=True)

    class Meta:
        model = Producto
        fields = [
            "id",
            "nombre",
            "description",
            "precio",
            "imagen",
            "categoria",
            "categoria_nombre"
        ]

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        categoria_obj = Categoria.objects.filter(slug=validated_data['categoria'].first())
        if not categoria_obj:
            raise serializers.ValidationError("Categoria no existe")

        producto = Producto.objects.create(
            nombre=validated_data["nombre"],
            precio=validated_data["precio"],
            categoria=categoria_obj,
            descripcion=validated_data["descripcion"],
        )
        return producto