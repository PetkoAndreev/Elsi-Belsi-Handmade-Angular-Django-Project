import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  //define the toogle class property
  toggleClass: boolean = false;

  get isLoggedIn(): boolean {
    return this.userService.isLoggedIn;
  }

  constructor(
    private router: Router,
    public userService: UserService,
  ) { }

  ngOnInit(): void { }

}
