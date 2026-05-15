from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Usuarios.models.carrito_model import Carrito, ItemCarrito
from Usuarios.serializers.carrito_serializers import CarritoSerializer, ItemCarritoSerializer
from Productos.models import Producto

class MiCarritoView(generics.RetrieveAPIView):
    serializer_class = CarritoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        carrito, created = Carrito.objects.get_or_create(usuario=self.request.user)
        return carrito

class AgregarItemCarritoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
        producto_id = request.data.get('producto')
        cantidad = int(request.data.get('cantidad', 1))

        if not producto_id:
            return Response({"error": "Debe enviar un producto"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            producto = Producto.objects.get(id=producto_id)
        except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
        if not created:
            item.cantidad += cantidad
            item.save()
        else:
            item.cantidad = cantidad
            item.save()

        return Response(CarritoSerializer(carrito).data, status=status.HTTP_200_OK)

class RemoverItemCarritoView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id, *args, **kwargs):
        carrito = Carrito.objects.get(usuario=request.user)
        try:
            item = ItemCarrito.objects.get(id=item_id, carrito=carrito)
            item.delete()
            return Response(CarritoSerializer(carrito).data, status=status.HTTP_200_OK)
        except ItemCarrito.DoesNotExist:
            return Response({"error": "Item no encontrado en el carrito"}, status=status.HTTP_404_NOT_FOUND)
