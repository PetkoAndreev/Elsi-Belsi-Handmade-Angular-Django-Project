import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductsPageComponent } from './products-page/products-page.component';
import { ProductItemComponent } from './product-item/product-item.component';
import { ProductsRoutingModule } from './products-routing.module';
import { ProductDetailsComponent } from './product-details/product-details.component';
import { FormsModule } from '@angular/forms';
import { ProductNewComponent } from './product-new/product-new.component'



@NgModule({
  declarations: [
    ProductsPageComponent,
    ProductItemComponent,
    ProductDetailsComponent,
    ProductNewComponent,
  ],
  imports: [
    CommonModule,
    ProductsRoutingModule,
    FormsModule,
  ]
})
export class ProductsModule { }
