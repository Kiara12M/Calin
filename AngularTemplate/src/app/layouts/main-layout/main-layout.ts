import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {Header} from "./components/header/header";
import {RouterOutlet} from "@angular/router";
import {Footer} from "./components/footer/footer";
import {CartComponent} from "../../shared/components/cart/cart.component";

@Component({
  selector: 'app-main-layout',
    imports: [
        CommonModule,
        Header,
        RouterOutlet,
        Footer,
        CartComponent
    ],
  templateUrl: './main-layout.html',
  styleUrl: './main-layout.scss',
    standalone: true
})
export class MainLayout {
    isCartOpen = false;

    toggleCart() {
        this.isCartOpen = !this.isCartOpen;
    }
}

