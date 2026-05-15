import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { CartService } from '../../../../core/services/cart.service';

@Component({
  selector: 'app-accesorios',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './accesorios.html',
  styleUrl: './accesorios.scss'
})
export class Accesorios {
    private cartService = inject(CartService);

    accesoriosList = [
        { id: 401, nombre: 'Prensa Francesa', descripcion: 'Sistema clásico para el mejor café', precio: 25.00, cantidad: 1 },
        { id: 402, nombre: 'Cafetera Italiana', descripcion: 'Elaboración tradicional en casa', precio: 18.50, cantidad: 1 },
        { id: 403, nombre: 'Juego de Tazas de Cerámica', descripcion: 'Diseño elegante y minimalista', precio: 14.00, cantidad: 1 },
        { id: 404, nombre: 'Latas Herméticas Premium', descripcion: 'Mantiene tus granos siempre frescos', precio: 9.95, cantidad: 1 },
        { id: 405, nombre: 'Filtros Reutilizables', descripcion: 'Tela ecológica para V60', precio: 6.50, cantidad: 1 }
    ];

    comprar(producto: any) {
        if (producto.cantidad > 0) {
            this.cartService.addToCart(producto, producto.cantidad);
            const originalNombre = producto.nombre;
            producto.nombre = "¡Añadido!";
            setTimeout(() => {
                producto.nombre = originalNombre;
            }, 1000);
        }
    }
}
