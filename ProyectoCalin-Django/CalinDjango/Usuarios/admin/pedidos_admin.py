from django.contrib import admin
from Usuarios.models.pedidos_model import Pedidos

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "fecha", "estado", "total")
    list_filter = ("estado", "fecha")
    search_fields = ("usuario_username", "email", "id")
    readonly_fields = ("fecha",) #fecha protegida, es para que no me lo editen
    list_per_page = 20

    ordering = ("-fecha",)

    fieldsets = (
    ("Información del usuario", {
        "fields": ("usuario",)
    }),
    ("Detalles del pedido", {
        "fields": ("fecha", "estado", "total", "direccion_envio")
    }),
    )

admin.site.register(Pedidos, PedidosAdmin)