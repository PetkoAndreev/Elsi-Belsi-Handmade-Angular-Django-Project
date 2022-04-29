import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { debounceTime, Observable, startWith, switchMap, tap } from 'rxjs';
import { IProduct } from 'src/app/core/interfaces';
import { AuthService } from 'src/app/core/services/auth.service';
import { ProductService } from 'src/app/core/services/product.service';

@Component({
  selector: 'app-products-page',
  templateUrl: './products-page.component.html',
  styleUrls: ['./products-page.component.css']
})
export class ProductsPageComponent implements OnInit {

  productList!: IProduct[];
  isLoggedIn$: Observable<boolean> = this.authService.isLoggedIn$;

  searchControl = new FormControl();

  constructor(
    private productService: ProductService,
    private authService: AuthService,
  ) { }

  ngOnInit(): void {
    this.searchControl.valueChanges
      .pipe(
        startWith(''),
        debounceTime(300),
        switchMap(searchTerm => this.productService.loadProductList(searchTerm))
      )
      .subscribe(productList => {
        this.productList = productList;
      });
  }
}
