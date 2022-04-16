import { Component } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
// import { AngularFaviconService } from 'angular-favicon';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'elsi-belsi-handmade';

  // Logic to check the URL and if it's not-found to hide header and footer.
  notFoundIsActive: boolean = false;
  constructor(private router: Router) {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        const url = event.urlAfterRedirects;
        this.notFoundIsActive = url === '/not-found' ? true : false;
      }
    });
  }
}