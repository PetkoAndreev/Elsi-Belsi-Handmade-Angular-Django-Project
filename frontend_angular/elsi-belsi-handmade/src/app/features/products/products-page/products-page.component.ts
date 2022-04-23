import { Component, OnInit } from '@angular/core';
import { IProduct } from 'src/app/core/interfaces';
import { ProductService } from 'src/app/core/services/product.service';

@Component({
  selector: 'app-products-page',
  templateUrl: './products-page.component.html',
  styleUrls: ['./products-page.component.css']
})
export class ProductsPageComponent implements OnInit {

  productList!: IProduct[];

  constructor(
    private productService: ProductService,
  ) { }

  ngOnInit(): void {
    this.productService.loadProductList().subscribe(productList => {
      this.productList = productList;
    })
  }
}
