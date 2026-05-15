import { Component, inject, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { CartService } from '../../../core/services/cart.service';
import { AuthService } from '../../../core/services/auth.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-cart',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent {
  public cartService = inject(CartService);
  private authService = inject(AuthService);
  private router = inject(Router);
  
  @Input() isOpen: boolean = false;
  @Output() closeCart = new EventEmitter<void>();

  onClose() {
    this.closeCart.emit();
  }

  removeItem(index: number) {
    this.cartService.removeFromCart(index, true); 
  }

  checkout() {
      if (this.cartService.cartItems().length === 0) return;
      
      if (!this.authService.isAuthenticated()) {
        this.onClose();
        Swal.fire({
          icon: 'warning',
          title: 'Inicia Sesión',
          text: 'Para finalizar tu compra, primero debes iniciar sesión o registrarte.',
          confirmButtonColor: '#9e7861',
          confirmButtonText: 'Ir a Iniciar Sesión'
        }).then(() => {
          this.router.navigate(['/login']);
        });
        return;
      }
      
      this.onClose(); // Cerrar el carrito lateral
      this.router.navigate(['/checkout']); // Navegar al checkout
  }
}

