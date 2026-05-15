from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Productos.models.pedido_models import Pedido
from Productos.serializers.pedido_serializers import PedidoSerializer

class MisPedidosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pedidos = Pedido.objects.filter(usuario=request.user).order_by('-creado')
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)
