import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CalinDjango.settings')
django.setup()

from Productos.models import Producto, Categoria

def seed():
    # Crear algunas categorías de prueba
    cat_cafe, _ = Categoria.objects.get_or_create(nombre='Café', slug='cafe')
    cat_te, _ = Categoria.objects.get_or_create(nombre='Té', slug='te')
    cat_acc, _ = Categoria.objects.get_or_create(nombre='Accesorios', slug='accesorios')

    # Crear algunos productos de prueba
    productos = [
        {'nombre': 'Café Espresso', 'description': 'Café intenso y aromático', 'precio': 12.50, 'is_active': True, 'categoria': cat_cafe},
        {'nombre': 'Café Arabica', 'description': 'Café suave 100% arabica', 'precio': 15.00, 'is_active': True, 'categoria': cat_cafe},
        {'nombre': 'Té Verde Matcha', 'description': 'Té verde en polvo ceremonial', 'precio': 18.00, 'is_active': True, 'categoria': cat_te},
        {'nombre': 'Té Negro Earl Grey', 'description': 'Té negro clásico con bergamota', 'precio': 9.50, 'is_active': True, 'categoria': cat_te},
        {'nombre': 'Taza de Cerámica', 'description': 'Taza artesanal para tus bebidas', 'precio': 25.00, 'is_active': True, 'categoria': cat_acc},
        {'nombre': 'Prensa Francesa', 'description': 'Cafetera de émbolo de vidrio', 'precio': 35.00, 'is_active': True, 'categoria': cat_acc},
    ]

    for data in productos:
        Producto.objects.get_or_create(nombre=data['nombre'], defaults=data)

    print("✅ Productos de prueba creados exitosamente.")

if __name__ == '__main__':
    seed()
