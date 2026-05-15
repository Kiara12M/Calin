from django.utils.text import slugify
from rest_framework.fields import CharField
from django.core.exceptions import ValidationError

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(unique=True, max_length=100, verbose_name="nombre")
    slug = models.SlugField(unique=True, verbose_name="slug")
    #padre = models.ForeigKey('self', on_delete=models.CASCADE, null=True, blank=True, realated_name='subcategorias')
    #para las subcategorias

    class Meta:
        db_table = "Categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = slugify(self.nombre)
            cont = 1

            while Categoria.objects.filter(slug=prov).exists():
                prov = slugify(self.nombre) + " " + str(cont)
                cont += 1
            self.slug = prov

            categoria = Categoria.objects.filter(nombre=self.nombre).first()
            if categoria and categoria.nombre == self.nombre:
                raise ValidationError({"nombre": ["El categoria ya existe"], })
        super().save(*args, **kwargs)