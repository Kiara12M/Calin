import { Component, Output, EventEmitter, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from "@angular/router";
import { CartService } from '../../../../core/services/cart.service';
import { AuthService } from '../../../../core/services/auth.service';

@Component({
  selector: 'app-header',
    imports: [
        CommonModule,
        RouterLink
    ],
  templateUrl: './header.html',
  styleUrl: './header.scss',
})
export class Header {
    @Output() toggleCart = new EventEmitter<void>();
    public cartService = inject(CartService);
    public authService = inject(AuthService);

    onToggleCart() {
        this.toggleCart.emit();
    }
}

