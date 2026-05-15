import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { CartService } from '../../../../core/services/cart.service';

@Component({
  selector: 'app-chocolates',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './chocolates.html',
  styleUrl: './chocolates.scss'
})
export class Chocolates {
    private cartService = inject(CartService);

    chocolatesList = [
        { id: 301, nombre: 'Tableta Chocolate Negro 85%', descripcion: 'Cacao puro y artesanía suiza', precio: 6.50, cantidad: 1 },
        { id: 302, nombre: 'Trufas de Caramelo Salado', descripcion: 'Explosión de sabor crujiente', precio: 12.00, cantidad: 1 },
        { id: 303, nombre: 'Chocolate Blanco con Frambuesa', descripcion: 'Dulce y suave con toques frutales', precio: 7.20, cantidad: 1 },
        { id: 304, nombre: 'Bombones Surtidos Venchi', descripcion: 'La mejor selección italiana', precio: 15.50, cantidad: 1 }
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
