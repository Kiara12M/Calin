import { Component, output} from '@angular/core';

@Component({
  selector: 'app-ayuda',
  imports: [],
  templateUrl: './ayuda.html',
  styleUrl: './ayuda.scss',
})
export class Ayuda {

    openAyudaDesdeHeader=output();
}
