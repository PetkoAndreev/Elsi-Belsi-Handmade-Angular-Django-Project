import { AfterViewInit, Component, ElementRef, OnInit } from '@angular/core';
import { IUser } from '../interfaces';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit, AfterViewInit {

  //define the toogle class property
  toggleClass: boolean = false;

  get isLoggedIn(): boolean {
    return this.userService.isLoggedIn;
  }

  get currentUser(): IUser {
    return this.userService.currentUser;
  }

  constructor(
    public userService: UserService,
    private elementRef: ElementRef,
  ) { }

  ngOnInit(): void { }

  // Added logic for load custom js files which comes from the theme.
  ngAfterViewInit() {
    let s = document.createElement("script");
    s.type = "text/javascript";
    s.src = "../../../assets/js/jquery.min.js";
    this.elementRef.nativeElement.appendChild(s);

    let s0 = document.createElement("script");
    s0.type = "text/javascript";
    s0.src = "../../../assets/js/bootstrap.bundle.min.js";
    this.elementRef.nativeElement.appendChild(s0);

    let s01 = document.createElement("script");
    s01.type = "text/javascript";
    s01.src = "../../../assets/js/Headroom.js";
    this.elementRef.nativeElement.appendChild(s01);

    let s1 = document.createElement("script");
    s1.type = "text/javascript";
    s1.src = "../../../assets/js/jQuery.headroom.js";
    this.elementRef.nativeElement.appendChild(s1);

    let s2 = document.createElement("script");
    s2.type = "text/javascript";
    s2.src = "../../../assets/js/slick.min.js";
    this.elementRef.nativeElement.appendChild(s2);

    let s3 = document.createElement("script");
    s3.type = "text/javascript";
    s3.src = "../../../assets/js/custom.js";
    this.elementRef.nativeElement.appendChild(s3);
  }

}
