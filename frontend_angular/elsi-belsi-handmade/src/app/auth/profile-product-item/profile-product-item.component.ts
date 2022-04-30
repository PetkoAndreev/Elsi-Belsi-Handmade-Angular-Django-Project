import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { IProduct } from 'src/app/core/interfaces';
import { AuthService } from 'src/app/core/services/auth.service';

@Component({
  selector: 'app-profile-product-item',
  templateUrl: './profile-product-item.component.html',
  styleUrls: ['./profile-product-item.component.css']
})
export class ProfileProductItemComponent implements OnInit {

  isLoggedIn$: Observable<boolean> = this.authService.isLoggedIn$;
  isLiked: boolean = false;
  isFavorite: boolean = false;

  @Input() product!: IProduct;

  constructor(
    private authService: AuthService,
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
