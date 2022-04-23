import { Injectable } from '@angular/core';

@Injectable()
export class UserService {

  isLoggedIn = false;

  constructor() { }

  login(): void {
    this.isLoggedIn = true;
  }

  logout(): void {
    this.isLoggedIn = false;
  }
}
