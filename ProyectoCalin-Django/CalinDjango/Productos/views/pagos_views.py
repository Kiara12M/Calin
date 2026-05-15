import time
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from Productos.models.pedido_models import Pedido, DetallePedido
from Productos.models.producto_models import Producto

class PagosView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Simulamos latencia de red para conectar con PayPal
        time.sleep(1.5)
        
        data = request.data
        monto = data.get("monto", 0)
        carrito = data.get("carrito", [])
        
        if monto <= 0 or not carrito:
            return Response(
                {"error": "Datos inválidos para procesar el pago."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Simular una respuesta exitosa de PayPal
        transaction_id = f"PAYID-{uuid.uuid4().hex.upper()[:17]}"
        
        try:
            with transaction.atomic():
                # Crear el pedido
                pedido = Pedido.objects.create(
                    usuario=request.user if request.user.is_authenticated else None,
                    total=monto,
                    estado="Pagado con PayPal",
                    transaction_id=transaction_id
                )
                
                # Crear los detalles
                for item in carrito:
                    producto_id = item.get("producto")
                    cantidad = item.get("cantidad", 1)
                    subtotal = item.get("subtotal", 0)
                    precio_unitario = float(subtotal) / float(cantidad) if cantidad > 0 else 0
                    
                    try:
                        producto_obj = Producto.objects.get(id=producto_id)
                    except Producto.DoesNotExist:
                        producto_obj = None
                        
                    DetallePedido.objects.create(
                        pedido=pedido,
                        producto=producto_obj,
                        cantidad=cantidad,
                        precio_unitario=precio_unitario
                    )
                    
            respuesta = {
                "status": "COMPLETED",
                "transaction_id": transaction_id,
                "message": "Pago procesado y pedido guardado correctamente",
                "monto_pagado": monto
            }
            return Response(respuesta, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {"error": "Error al guardar el pedido en la base de datos.", "detalle": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
