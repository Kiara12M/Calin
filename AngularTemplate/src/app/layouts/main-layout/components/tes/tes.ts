import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { CartService } from '../../../../core/services/cart.service';

@Component({
  selector: 'app-tes',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './tes.html',
  styleUrl: './tes.scss',
})
export class Tes {
    private cartService = inject(CartService);

    tesList = [
        { id: 201, nombre: 'Té Negro Ceylon', descripcion: 'Intenso y robusto', precio: 5.50, cantidad: 1 },
        { id: 202, nombre: 'Té Verde Matcha', descripcion: 'Puro de Japón, antioxidante', precio: 15.00, cantidad: 1 },
        { id: 203, nombre: 'Té Rojo Pu-erh', descripcion: 'Añejado, notas terrosas', precio: 8.20, cantidad: 1 },
        { id: 204, nombre: 'Té Oolong', descripcion: 'Té azul semi-fermentado', precio: 10.50, cantidad: 1 },
        { id: 205, nombre: 'Infusión Frutos Rojos', descripcion: 'Refrescante y sin teína', precio: 6.95, cantidad: 1 }
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
