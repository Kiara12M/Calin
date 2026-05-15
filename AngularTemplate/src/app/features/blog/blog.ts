import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-blog',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './blog.html',
  styles: [`
    .blog-header {
      background-color: #f5f1e8;
      padding: 4rem 0;
      border-radius: 1rem;
      margin-bottom: 3rem;
    }
  `]
})
export class Blog {
  posts = [
    {
      title: 'El origen de nuestro Té Matcha',
      date: '12 May, 2026',
      excerpt: 'Descubre el proceso tradicional detrás del mejor matcha ceremonial de Japón. Te contamos cómo seleccionamos nuestras hojas...',
      image: '/columna2_new.png'
    },
    {
      title: 'Diferencias entre Arábica y Robusta',
      date: '05 May, 2026',
      excerpt: 'Aprende a distinguir los dos tipos principales de granos de café y descubre cuál se adapta mejor a tu paladar.',
      image: '/portada3-cafes.jpg'
    },
    {
      title: 'Receta: Chocolate Caliente Perfecto',
      date: '28 Abr, 2026',
      excerpt: 'Te enseñamos nuestra receta secreta para preparar el chocolate a la taza más espeso y delicioso para los días fríos.',
      image: '/portada1.1-tazas.jpg'
    }
  ];
}
