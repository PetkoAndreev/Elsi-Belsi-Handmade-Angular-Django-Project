import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { FaqComponent } from './faq/faq.component';
import { AboutComponent } from './about/about.component';
import { ContactComponent } from './contact/contact.component';
import { PolicyComponent } from './policy/policy.component';



@NgModule({
  declarations: [
    HomePageComponent,
    PageNotFoundComponent,
    FaqComponent,
    AboutComponent,
    ContactComponent,
    PolicyComponent,
  ],
  imports: [
    CommonModule,
    RouterModule,
  ],
  exports: [
  ]
})
export class PagesModule { }
