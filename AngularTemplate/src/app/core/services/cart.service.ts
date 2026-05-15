import { Injectable, inject, signal, effect } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AuthService } from './auth.service';
import { Observable, of, tap } from 'rxjs';

export interface CartItem {
    id?: number;
    producto: number;
    producto_detalle?: any;
    cantidad: number;
    subtotal?: number;
}

import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  private http = inject(HttpClient);
  private authService = inject(AuthService);
  private readonly API_URL = environment.apiURL + 'carrito/';

  // Estado del carrito reactivo
  cartItems = signal<CartItem[]>([]);
  cartTotal = signal<number>(0);

  constructor() {
      // Cargar el carrito inicial
      this.loadCart();

      // Guardar en localstorage si cambia el carrito y no estamos logueados
      effect(() => {
          const items = this.cartItems();
          if (!this.authService.isAuthenticated()) {
             if (typeof window !== 'undefined') {
                 localStorage.setItem('calin_cart', JSON.stringify(items));
             }
          }
      });
  }

  private getHeaders() {
      const token = this.authService.getToken();
      return new HttpHeaders().set('Authorization', `Bearer ${token}`);
  }

  loadCart() {
      if (this.authService.isAuthenticated()) {
          // Descargar del backend
          this.http.get<any>(this.API_URL, { headers: this.getHeaders() }).subscribe({
              next: (cart) => {
                  this.cartItems.set(cart.items || []);
                  this.cartTotal.set(cart.total || 0);
              },
              error: () => console.error("Error cargando carrito")
          });
      } else {
          // Cargar de localstorage
          if (typeof window !== 'undefined') {
              const localCart = localStorage.getItem('calin_cart');
              if (localCart) {
                  this.cartItems.set(JSON.parse(localCart));
                  this.updateLocalTotal();
              }
          }
      }
  }

  addToCart(producto: any, cantidad: number = 1) {
      if (this.authService.isAuthenticated()) {
          this.http.post<any>(`${this.API_URL}agregar/`, { producto: producto.id, cantidad }, { headers: this.getHeaders() })
          .subscribe({
              next: (cart) => {
                  this.cartItems.set(cart.items);
                  this.cartTotal.set(cart.total);
              },
              error: (err) => {
                  console.error('Error al añadir al carrito:', err);
                  import('sweetalert2').then(Swal => {
                      Swal.default.fire('Error', 'No se pudo añadir el producto. Inténtalo de nuevo.', 'error');
                  });
              }
          });
      } else {
          // Logica para local storage
          const items = [...this.cartItems()];
          const existingItem = items.find(i => i.producto === producto.id);
          if (existingItem) {
              existingItem.cantidad += cantidad;
              existingItem.subtotal = existingItem.cantidad * producto.precio;
          } else {
              items.push({
                  producto: producto.id,
                  producto_detalle: producto,
                  cantidad: cantidad,
                  subtotal: producto.precio * cantidad
              });
          }
          this.cartItems.set(items);
          this.updateLocalTotal();
      }
  }

  removeFromCart(itemId: number, isLocalIndex: boolean = false) {
      if (this.authService.isAuthenticated() && !isLocalIndex) {
          this.http.delete<any>(`${this.API_URL}item/${itemId}/`, { headers: this.getHeaders() })
          .subscribe({
              next: (cart) => {
                  this.cartItems.set(cart.items);
                  this.cartTotal.set(cart.total);
              }
          });
      } else {
          let items = [...this.cartItems()];
          items.splice(itemId, 1);
          this.cartItems.set(items);
          this.updateLocalTotal();
      }
  }

  private updateLocalTotal() {
      const total = this.cartItems().reduce((acc, item) => acc + (item.subtotal || 0), 0);
      this.cartTotal.set(total);
  }

  getMisPedidos(): Observable<any> {
      const token = this.authService.getToken();
      const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);
      return this.http.get<any>(`${environment.apiURL}productos/mis-pedidos/`, { headers });
  }
}
