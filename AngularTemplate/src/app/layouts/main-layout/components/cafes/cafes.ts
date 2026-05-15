import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { CartService } from '../../../../core/services/cart.service';

@Component({
  selector: 'app-cafes',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './cafes.html',
  styleUrl: './cafes.scss',
})
export class Cafes {
    public cartService = inject(CartService);

    cafesNaturales = [
        { id: 101, nombre: 'Café Colombia', descripcion: 'Suave y equilibrado.', precio: 8, cantidad: 1 },
        { id: 102, nombre: 'Café Perú', descripcion: 'Aromático y dulce.', precio: 5, cantidad: 1 },
        { id: 103, nombre: 'Café Etiopía', descripcion: 'Notas florales.', precio: 11.5, cantidad: 1 },
        { id: 104, nombre: 'Café Brasil', descripcion: 'Cuerpo medio.', precio: 9.65, cantidad: 1 }
    ];

    cafesAromatizados = [
        { id: 105, nombre: 'Café Vainilla', descripcion: 'Sabor aromático dulce', precio: 7.5, cantidad: 1 },
        { id: 106, nombre: 'Café Caramelo', descripcion: 'Notas tostadas', precio: 8, cantidad: 1 }
    ];

    cafesVerdes = [
        { id: 107, nombre: 'Café Verde Detox', descripcion: 'Café sin tostar, muy sano', precio: 10.5, cantidad: 1 }
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
