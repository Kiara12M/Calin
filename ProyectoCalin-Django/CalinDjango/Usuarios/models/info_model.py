from django.db import models


class PaisesChoices(models.TextChoices):
    SPAIN = "ES", "ESPAÑA"
    ENGLAND = "EN", "INGLATERRA"
    CHINA = "CH", "CHINA"
    FRANCE = "FR", "FRANCE"

class InfoPersonal(models.Model):
    telefono = models.CharField(max_length=6, null=True, blank=True, verbose_name="Teléfono")

    direccion = models.TextField(null=False, blank=False, verbose_name="Dirección")

    #ciudad = models.ForeignKey("Ciudad", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ciudad")

    pais = models.CharField(max_length=3, choices=PaisesChoices.choices, default=PaisesChoices.SPAIN,
                            verbose_name="País", null=False, blank=False, help_text="(Obligatorio)")

    class Meta:
        db_table = "infoPersonal"
        verbose_name = "Dato"
        verbose_name_plural = "Datos"
        ordering = ["telefono"]

    def __str__(self):
        return f"{self.telefono} {self.direccion}"