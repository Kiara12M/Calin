from django.contrib import admin
from Productos.models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    readonly_fields = ('slug',)

admin.site.register(Categoria, CategoriaAdmin)
