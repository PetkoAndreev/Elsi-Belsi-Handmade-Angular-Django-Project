import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { IProfile } from 'src/app/core/interfaces';
import { UserService } from 'src/app/core/services/user.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  currentUser!: IProfile;

  isInEditMode: boolean = false;

  constructor(
    private userService: UserService,
    private activatedRoute: ActivatedRoute,
    private router: Router,
  ) { }

  ngOnInit(): void {
    this.activatedRoute.params.subscribe(params => {
      const profileId = params['productId'];
      this.userService.getProfile$(profileId).subscribe({
        next: (user) => {
          this.currentUser = user
        },
        error: () => {
          this.router.navigate(['/login'])
        }
      })
    })
  }


  updateProfile(): void {

  }

  exitEditMode(): void {

  }

}
