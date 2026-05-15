from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos', blank=True, null=True,
                                  verbose_name="Categoria")
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True, verbose_name="Slug")
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    categoria = models.ForeignKey("Categoria", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'productos'
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-categoria__nombre', '-nombre']


    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = slugify(self.nombre)
            cont = 1

            while Producto.objects.filter(slug=prov).exists():
                prov = slugify(self.nombre) + " " + str(cont)
                cont += 1
            self.slug = prov

            producto = Producto.objects.filter(nombre=self.nombre).exclude(pk=self.pk).first()
            if producto:
                raise ValidationError({"nombre": ["El producto ya existe"], })
        super().save(*args, **kwargs)