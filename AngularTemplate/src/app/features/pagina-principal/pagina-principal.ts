import { Component, AfterViewInit, Inject, PLATFORM_ID } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import { RouterLink } from "@angular/router";

declare var bootstrap: any;

@Component({
  selector: 'app-pagina-principal',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './pagina-principal.html',
  styleUrl: './pagina-principal.scss',
})
export class PaginaPrincipal implements AfterViewInit {

    constructor(@Inject(PLATFORM_ID) private platformId: Object) {}

    ngAfterViewInit() {
        if (isPlatformBrowser(this.platformId)) {
            const carouselElement = document.querySelector('#carouselIndicators');
            if (carouselElement) {
                new bootstrap.Carousel(carouselElement, {
                    interval: 4000,
                    ride: 'carousel'
                });
            }
        }
    }
}
