import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { IProduct } from 'src/app/core/interfaces';
import { AuthService } from 'src/app/core/services/auth.service';
import { ProductService } from 'src/app/core/services/product.service';

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.css']
})
export class ProductDetailsComponent implements OnInit {

  @ViewChild('editProductForm') editProductForm!: NgForm;

  isInEditMode: boolean = false;
  product!: IProduct;
  isLoggedIn$: Observable<boolean> = this.authService.isLoggedIn$

  constructor(
    private activatedRoute: ActivatedRoute,
    private productService: ProductService,
    private authService: AuthService,
  ) { }

  ngOnInit(): void {
    // Get dinamically product id with ActivatedRoute
    this.activatedRoute.params.subscribe(params => {
      const productId = params['productId'];
      this.productService.loadProductById$(productId).subscribe(product => {
        this.product = product;
        console.log(product)
      });
    })
  }

  enterEditMode(): void {
    this.isInEditMode = true;

    setTimeout(() => {
      this.editProductForm.form.patchValue({
        productName: this.product.product_name,
        productCategory: this.product.prd_category,
        productDescription: this.product.prd_description,
        productPrice: this.product.prd_price,
        productDiscount: this.product.prd_discount,
        productImage: this.product.prd_image,
      })
    });
  }

  updateProduct(): void {
    this.isInEditMode = false;
  }
}