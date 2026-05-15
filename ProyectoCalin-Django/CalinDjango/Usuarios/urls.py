from django.urls import path
from Usuarios.views.register_view import RegisterView
from Usuarios.views.carrito_views import MiCarritoView, AgregarItemCarritoView, RemoverItemCarritoView

urlpatterns = [
    path('usuarios/register/', RegisterView.as_view(), name='register'),
    path('carrito/', MiCarritoView.as_view(), name='mi_carrito'),
    path('carrito/agregar/', AgregarItemCarritoView.as_view(), name='carrito_agregar'),
    path('carrito/item/<int:item_id>/', RemoverItemCarritoView.as_view(), name='carrito_remover'),
]
