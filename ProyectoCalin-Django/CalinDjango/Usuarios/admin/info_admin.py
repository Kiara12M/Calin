from django.contrib import admin
from Usuarios.models import CustomUser
from Usuarios.models.info_model import InfoPersonal


class InfoAdmin(admin.ModelAdmin):
    list_display = ("user", "telefono", "direccion", "pais")
    search_fields = ("telefono",)
    list_filter = ("pais",)

    list_per_page = 20

    fieldsets = (
        ("Información personal", {
            "classes": ("wide",),
            "fields": ("telefono", "direccion", "pais")
        }),
    )

    @admin.display(description="Usuario")
    def user(self, obj):
        return CustomUser.objects.get(personal_info=obj).email



admin.site.register(InfoPersonal, InfoAdmin)