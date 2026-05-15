import { Injectable, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap, catchError, throwError } from 'rxjs';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private http = inject(HttpClient);

  // Signals para verificar el estado de inicio de sesión de forma reactiva
  isAuthenticated = signal<boolean>(this.hasToken());

  private hasToken(): boolean {
    if (typeof window !== 'undefined') {
        return !!localStorage.getItem('access_token');
    }
    return false;
  }

  register(userData: any): Observable<any> {
    return this.http.post(`${environment.apiURL}usuarios/register/`, userData);
  }

  login(credentials: any): Observable<any> {
    return this.http.post(`${environment.apiURL}token/`, credentials).pipe(
      tap((response: any) => {
        if(response.access) {
            if (typeof window !== 'undefined') {
                localStorage.setItem('access_token', response.access);
                localStorage.setItem('refresh_token', response.refresh);
                this.isAuthenticated.set(true);
            }
        }
      })
    );
  }

  logout() {
    if (typeof window !== 'undefined') {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        this.isAuthenticated.set(false);
    }
  }

  getToken(): string | null {
    if (typeof window !== 'undefined') {
        return localStorage.getItem('access_token');
    }
    return null;
  }
}
