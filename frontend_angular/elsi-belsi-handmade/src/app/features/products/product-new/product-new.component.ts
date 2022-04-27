import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { ProductService } from 'src/app/core/services/product.service';

@Component({
  selector: 'app-product-new',
  templateUrl: './product-new.component.html',
  styleUrls: ['./product-new.component.css']
})
export class ProductNewComponent implements OnInit {

  constructor(
    private router: Router,
    private productService: ProductService,
  ) { }

  ngOnInit(): void {
  }

  submitNewProduct(newProductForm: NgForm): void {
    this.productService.addProduct$(newProductForm.value).subscribe({
      next: (product) => {
        console.log(product);
        this.router.navigate(['/products'])
      },
      error: (err) => {
        console.log(err);
      }
    })
  }

  navigateToHome(): void {
    this.router.navigate(['/home'])
  }

}
