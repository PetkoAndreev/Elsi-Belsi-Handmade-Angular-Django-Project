import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { IProduct } from 'src/app/core/interfaces';
import { AuthService } from 'src/app/core/services/auth.service';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {

  isLoggedIn$: Observable<boolean> = this.authService.isLoggedIn$;
  isLiked: boolean = false;
  isFavorite: boolean = true;

  @Input() product!: IProduct;

  constructor(
    private authService: AuthService,
  ) { }

  ngOnInit(): void {
  }
}
