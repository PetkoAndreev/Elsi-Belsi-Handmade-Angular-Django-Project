import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WelcomeComponent } from './welcome/welcome.component';

@NgModule({
  declarations: [
    // 13.04. - Added Welcome Component
    WelcomeComponent,
  ],
  imports: [
    CommonModule
  ],
  exports: [
    // 13.04. - Added Welcome Component
    WelcomeComponent,
  ]
})
export class SharedModule { }