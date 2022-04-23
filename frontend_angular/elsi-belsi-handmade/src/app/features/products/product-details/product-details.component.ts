import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { IProduct } from 'src/app/core/interfaces';
import { ProductService } from 'src/app/core/services/product.service';
import { UserService } from 'src/app/core/services/user.service';

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.css']
})
export class ProductDetailsComponent implements OnInit {

  product!: IProduct;
  isLoggedIn: boolean = this.userService.isLoggedIn

  constructor(
    private activatedRoute: ActivatedRoute,
    private productService: ProductService,
    private userService: UserService,
  ) { }

  ngOnInit(): void {
    // Get dinamically product id with ActivatedRoute
    this.activatedRoute.params.subscribe(params => {
      const productId = params['productId'];
      this.productService.loadProductById(productId).subscribe(product => {
        this.product = product;
      });
    })

  }

}
