import { Component, Input, OnInit } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { IProduct } from 'src/app/core/interfaces';
import { AuthService } from 'src/app/core/services/auth.service';
import { ProductService } from 'src/app/core/services/product.service';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {

  isLoggedIn$: Observable<boolean> = this.authService.isLoggedIn$;
  isLiked: boolean = false;
  isFavorite: boolean = false;

  @Input() product!: IProduct;

  constructor(
    private authService: AuthService,
    private productService: ProductService,
  ) { }

  ngOnInit(): void {
  }

  like(): void {
    this.isLiked = !this.isLiked
  }

  addToFavorites(): void {
    this.isFavorite = !this.isFavorite
  }
}
