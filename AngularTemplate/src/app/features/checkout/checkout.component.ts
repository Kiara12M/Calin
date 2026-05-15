import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CartService } from '../../core/services/cart.service';
import { AuthService } from '../../core/services/auth.service';
import { environment } from '../../../environments/environment';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-checkout',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.scss']
})
export class CheckoutComponent implements OnInit {
  checkoutForm!: FormGroup;
  step: number = 1;

  public cartService = inject(CartService);
  private router = inject(Router);
  private fb = inject(FormBuilder);
  private http = inject(HttpClient);
  private authService = inject(AuthService);

  ngOnInit() {
    // Si el carrito está vacío o no está logueado, redirigir
    if (this.cartService.cartItems().length === 0 || !this.authService.isAuthenticated()) {
      this.router.navigate(['/']);
    }

    this.checkoutForm = this.fb.group({
      nombre: ['', Validators.required],
      apellidos: ['', Validators.required],
      direccion: ['', Validators.required],
      ciudad: ['', Validators.required],
      codigoPostal: ['', Validators.required],
      titular: ['', Validators.required],
      numeroTarjeta: ['', [Validators.required, Validators.pattern('^[0-9]{16}$')]],
      caducidad: ['', [Validators.required, Validators.pattern('^(0[1-9]|1[0-2])\/?([0-9]{2})$')]],
      cvv: ['', [Validators.required, Validators.pattern('^[0-9]{3,4}$')]]
    });
  }

  nextStep() {
    if (this.checkoutForm.valid) {
      this.step = 2;
    } else {
      this.checkoutForm.markAllAsTouched();
    }
  }

  prevStep() {
    this.step = 1;
  }

  confirmarPago() {
    Swal.fire({
      title: 'Procesando pago...',
      text: 'Conectando con la pasarela de pagos (Simulación)',
      allowOutsideClick: false,
      didOpen: () => {
        Swal.showLoading();
      }
    });

    const payload = {
      monto: this.cartService.cartTotal(),
      carrito: this.cartService.cartItems(),
      datos_envio: this.checkoutForm.value
    };

    const token = this.authService.getToken();
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${token}`
    });

    this.http.post<any>(`${environment.apiURL}productos/pagos/paypal/`, payload, { headers }).subscribe({
      next: (res) => {
        Swal.fire({
          icon: 'success',
          title: '¡Pago Exitoso!',
          text: `Transacción: ${res.transaction_id}. Tu pedido está en camino.`,
          confirmButtonColor: '#9e7861'
        }).then(() => {
          this.cartService.cartItems.set([]);
          this.cartService.cartTotal.set(0);
          if (typeof window !== 'undefined') localStorage.removeItem('calin_cart');
          this.router.navigate(['/']);
        });
      },
      error: (err) => {
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'Hubo un problema al procesar el pago.',
          confirmButtonColor: '#9e7861'
        });
        this.step = 1;
      }
    });
  }
}
