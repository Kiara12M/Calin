import { Component, inject, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CartService } from '../../core/services/cart.service';

@Component({
  selector: 'app-mis-pedidos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './mis-pedidos.component.html',
  styleUrls: ['./mis-pedidos.component.scss']
})
export class MisPedidosComponent implements OnInit {
  public cartService = inject(CartService);
  private cdr = inject(ChangeDetectorRef);
  pedidos: any[] = [];
  loading = true;
  error = '';

  ngOnInit() {
    this.cartService.getMisPedidos().subscribe({
      next: (res) => {
        this.pedidos = res;
        this.loading = false;
        this.cdr.markForCheck();
      },
      error: (err) => {
        this.error = 'Error al cargar los pedidos. Por favor, inténtalo de nuevo.';
        this.loading = false;
        this.cdr.markForCheck();
      }
    });
  }
}
