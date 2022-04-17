import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';



@NgModule({
  declarations: [
    HomePageComponent,
    PageNotFoundComponent,
  ],
  imports: [
    CommonModule,
    RouterModule,
  ],
  exports: []
})
export class PagesModule { }
