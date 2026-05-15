import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CalinDjango.settings')
django.setup()

from Productos.models import Producto, Categoria

def seed():
    cat_cafe, _ = Categoria.objects.get_or_create(nombre='Café', slug='cafe')
    cat_te, _ = Categoria.objects.get_or_create(nombre='Té', slug='te')
    cat_choc, _ = Categoria.objects.get_or_create(nombre='Chocolate', slug='chocolate')
    cat_acc, _ = Categoria.objects.get_or_create(nombre='Accesorios', slug='accesorios')

    productos = [
        # Cafes
        {'id': 101, 'nombre': 'Café Colombia', 'description': 'Suave y equilibrado.', 'precio': 8.00, 'categoria': cat_cafe},
        {'id': 102, 'nombre': 'Café Perú', 'description': 'Aromático y dulce.', 'precio': 5.00, 'categoria': cat_cafe},
        {'id': 103, 'nombre': 'Café Etiopía', 'description': 'Notas florales.', 'precio': 11.50, 'categoria': cat_cafe},
        {'id': 104, 'nombre': 'Café Brasil', 'description': 'Cuerpo medio.', 'precio': 9.65, 'categoria': cat_cafe},
        {'id': 105, 'nombre': 'Café Vainilla', 'description': 'Sabor aromático dulce', 'precio': 7.50, 'categoria': cat_cafe},
        {'id': 106, 'nombre': 'Café Caramelo', 'description': 'Notas tostadas', 'precio': 8.00, 'categoria': cat_cafe},
        {'id': 107, 'nombre': 'Café Verde Detox', 'description': 'Café sin tostar, muy sano', 'precio': 10.50, 'categoria': cat_cafe},
        # Tes
        {'id': 201, 'nombre': 'Té Negro Ceylon', 'description': 'Intenso y robusto', 'precio': 5.50, 'categoria': cat_te},
        {'id': 202, 'nombre': 'Té Verde Matcha', 'description': 'Puro de Japón, antioxidante', 'precio': 15.00, 'categoria': cat_te},
        {'id': 203, 'nombre': 'Té Rojo Pu-erh', 'description': 'Añejado, notas terrosas', 'precio': 8.20, 'categoria': cat_te},
        {'id': 204, 'nombre': 'Té Oolong', 'description': 'Té azul semi-fermentado', 'precio': 10.50, 'categoria': cat_te},
        {'id': 205, 'nombre': 'Infusión Frutos Rojos', 'description': 'Refrescante y sin teína', 'precio': 6.95, 'categoria': cat_te},
        # Chocolates
        {'id': 301, 'nombre': 'Tableta Chocolate Negro 85%', 'description': 'Cacao puro y artesanía suiza', 'precio': 6.50, 'categoria': cat_choc},
        {'id': 302, 'nombre': 'Trufas de Caramelo Salado', 'description': 'Explosión de sabor crujiente', 'precio': 12.00, 'categoria': cat_choc},
        {'id': 303, 'nombre': 'Chocolate Blanco con Frambuesa', 'description': 'Dulce y suave con toques frutales', 'precio': 7.20, 'categoria': cat_choc},
        {'id': 304, 'nombre': 'Bombones Surtidos Venchi', 'description': 'La mejor selección italiana', 'precio': 15.50, 'categoria': cat_choc},
        # Accesorios
        {'id': 401, 'nombre': 'Prensa Francesa', 'description': 'Sistema clásico para el mejor café', 'precio': 25.00, 'categoria': cat_acc},
        {'id': 402, 'nombre': 'Cafetera Italiana', 'description': 'Elaboración tradicional en casa', 'precio': 18.50, 'categoria': cat_acc},
        {'id': 403, 'nombre': 'Juego de Tazas de Cerámica', 'description': 'Diseño elegante y minimalista', 'precio': 14.00, 'categoria': cat_acc},
        {'id': 404, 'nombre': 'Latas Herméticas Premium', 'description': 'Mantiene tus granos siempre frescos', 'precio': 9.95, 'categoria': cat_acc},
        {'id': 405, 'nombre': 'Filtros Reutilizables', 'description': 'Tela ecológica para V60', 'precio': 6.50, 'categoria': cat_acc},
    ]

    for data in productos:
        Producto.objects.update_or_create(
            id=data['id'],
            defaults={
                'nombre': data['nombre'],
                'description': data['description'],
                'precio': data['precio'],
                'categoria': data['categoria'],
                'is_active': True
            }
        )

    print("✅ Productos sincronizados exitosamente.")

if __name__ == '__main__':
    seed()
