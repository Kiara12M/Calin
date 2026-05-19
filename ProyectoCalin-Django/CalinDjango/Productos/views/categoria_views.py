from Productos.models import Categoria
from Productos.serializers import CategoriaSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class CategoriaView(APIView):

    def get(self, request):
        categorias = Categoria.objects.all().order_by("nombre")
        serializer = CategoriaSerializer(categorias, many=True)

        return Response(serializer.data)