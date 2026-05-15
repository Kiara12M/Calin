import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment} from "../../../../environments/environment";
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root',
})
export class ProductosService {

  private URL = environment.apiURL;

  constructor(private http: HttpClient) {
  }

}

