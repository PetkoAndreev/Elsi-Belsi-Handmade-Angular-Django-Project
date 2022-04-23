import { Component, Input, OnInit } from '@angular/core';
import { IProduct } from 'src/app/core/interfaces';
import { UserService } from 'src/app/core/services/user.service';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {

  isLoggedIn: boolean = this.userService.isLoggedIn;
  isLiked: boolean = false;
  isFavorite: boolean = true;

  @Input() product!: IProduct;

  constructor(
    private userService: UserService,
  ) { }

  ngOnInit(): void {
  }
}
