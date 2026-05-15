from django.urls import path
from Productos.views.categoria_views import CategoriaView
from Productos.views.pagos_views import PagosView
from Productos.views.pedidos_views import MisPedidosView

urlpatterns = [
    path("categorias/", CategoriaView.as_view(), name="categorias"),
    path("pagos/paypal/", PagosView.as_view(), name="pagos-paypal"),
    path("mis-pedidos/", MisPedidosView.as_view(), name="mis-pedidos"),
]
