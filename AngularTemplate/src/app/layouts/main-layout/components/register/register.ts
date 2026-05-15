import { Component, inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../../../core/services/auth.service';
import Swal from 'sweetalert2';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule, RouterLink],
  templateUrl: './register.html',
  styleUrl: './register.scss',
})
export class Register {
  registerForm: FormGroup;
  private fb = inject(FormBuilder);
  private authService = inject(AuthService);
  private router = inject(Router);

  constructor() {
    this.registerForm = this.fb.group({
      nombre: ['', Validators.required],
      apellidos: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      confirmPassword: ['', Validators.required]
    }, { validators: this.passwordMatchValidator });
  }

  passwordMatchValidator(g: FormGroup) {
    return g.get('password')?.value === g.get('confirmPassword')?.value
      ? null : { mismatch: true };
  }

  onSubmit() {
    if (this.registerForm.valid) {
      const userData = this.registerForm.value;
      this.authService.register(userData).subscribe({
        next: (res: any) => {
          Swal.fire({
            title: '¡Éxito!',
            text: 'Cuenta creada correctamente. Ahora puedes iniciar sesión.',
            icon: 'success',
            confirmButtonColor: '#5a4634'
          }).then(() => {
            this.router.navigate(['/login']);
          });
        },
        error: (err: any) => {
          Swal.fire({
            title: 'Error',
            text: err.error?.email ? 'Ese correo ya está en uso' : 'Hubo un error al crear la cuenta',
            icon: 'error',
            confirmButtonColor: '#9e7861'
          });
        }
      });
    } else {
      this.registerForm.markAllAsTouched();
    }
  }
}
