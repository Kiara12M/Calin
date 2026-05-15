from django.contrib import admin

from Productos.models import Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'is_active', 'creado', 'actualizado')
    readonly_fields = ('slug', 'creado', 'actualizado')
    list_editable = ('is_active',)

admin.site.register(Producto, ProductoAdmin)
