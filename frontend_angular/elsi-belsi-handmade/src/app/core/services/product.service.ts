import { HttpClient, HttpParams } from '@angular/common/http';
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

  addProduct$(body: { productName: string, productCategory: string, productDescription: string, productPrice: number, productDiscount?: number, productImage?: any }): Observable<IProduct> {
    return this.http.post<IProduct>(`${apiUrl}/products/`, body, { withCredentials: true })
  }

  loadProductList(searchTerm: string = ''): Observable<IProduct[]> {
    return this.http.get<IProduct[]>(`${apiUrl}/products/`, {
      params: new HttpParams({
        fromObject: {
          search: searchTerm, 
          // 'price-range': 'not-cheap' 
        }
      })
    });
  }

  loadProductById$(id: number): Observable<IProduct> {
    return this.http.get<IProduct>(`${apiUrl}/products/${id}/`);
  }

  likeProduct(id: number): Observable<void> {
    return this.http.put<void>(`${apiUrl}/products/${id}/`, {}, { withCredentials: true });
  }
}
