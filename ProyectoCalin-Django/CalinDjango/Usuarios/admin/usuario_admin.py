from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Usuarios.models import CustomUser
from Productos.models.pedido_models import Pedido


class PedidoInline(admin.TabularInline):
    model = Pedido
    extra = 0
    readonly_fields = ('total', 'estado', 'transaction_id', 'creado')
    can_delete = False
    show_change_link = True

class CustomUserAdmin(UserAdmin):
    list_display = ("nombre", "apellidos", "email", "is_active","is_staff", "is_superuser")
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("nombre", "apellidos", "email")

    list_editable = ("is_active", "is_staff", "is_superuser")

    list_per_page = 20

    ordering=("-email",)

    inlines = [PedidoInline]

    fieldsets = (
        ("Inicio de sesión", {"fields": ("email", "password")}),
        ("Información personal", {"fields": ("nombre", "apellidos")}),
        ("Configuración", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        ("Información personal", {
            'classes': ('wide',),
            'fields': ('nombre', 'apellidos')}
        ),
        ("Información de iniciar sesión", {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
        ("Configuración", {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)