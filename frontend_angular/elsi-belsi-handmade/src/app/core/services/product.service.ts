import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { IProduct } from '../interfaces';

const apiUrl = environment.apiUrl;

@Injectable()
export class ProductService {

  constructor(
    private http: HttpClient,
  ) { }

  loadProductList(): Observable<IProduct[]> {
    return this.http.get<IProduct[]>(`${apiUrl}/products/`);
  }
  loadProductById(id: number): Observable<IProduct> {
    return this.http.get<IProduct>(`${apiUrl}/products/${id}/`);
  }
}
