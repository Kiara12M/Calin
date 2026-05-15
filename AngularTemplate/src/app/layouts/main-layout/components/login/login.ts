import { Component, inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../../../core/services/auth.service';
import Swal from 'sweetalert2';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule, RouterLink],
  templateUrl: './login.html',
  styleUrl: './login.scss',
})
export class Login {
  loginForm: FormGroup;
  private fb = inject(FormBuilder);
  private authService = inject(AuthService);
  private router = inject(Router);

  constructor() {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

  onSubmit() {
    if (this.loginForm.valid) {
      this.authService.login(this.loginForm.value).subscribe({
        next: (res: any) => {
          Swal.fire({
            title: '¡Bienvenido!',
            text: 'Has iniciado sesión correctamente.',
            icon: 'success',
            timer: 1500,
            showConfirmButton: false
          }).then(() => {
            this.router.navigate(['/']);
          });
        },
        error: (err: any) => {
          Swal.fire({
            title: 'Error de Autenticación',
            text: 'El correo electrónico o la contraseña son incorrectos.',
            icon: 'error',
            confirmButtonColor: '#9e7861'
          });
        }
      });
    } else {
      this.loginForm.markAllAsTouched();
    }
  }
}
