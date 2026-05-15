import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-quienes-somos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './quienes-somos.html',
  styles: [`
    .faq-container { background-color: #fcfbf8; }
    .accordion-button:not(.collapsed) {
      color: #5a4634;
      background-color: #f5f1e8;
      box-shadow: inset 0 -1px 0 rgba(0,0,0,.125);
    }
  `]
})
export class QuienesSomos {
}
