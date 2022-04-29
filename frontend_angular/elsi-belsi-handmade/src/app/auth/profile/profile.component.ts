import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { IProfile } from 'src/app/core/interfaces';
import { UserService } from 'src/app/core/services/user.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  @ViewChild('editProfileForm') editProfileForm!: NgForm;

  currentUser!: IProfile;

  isInEditMode: boolean = false;

  constructor(
    private userService: UserService,
    private activatedRoute: ActivatedRoute,
    private router: Router,
  ) { }

  ngOnInit(): void {
    console.log(localStorage.getItem('access'))
    this.userService.getProfile$().subscribe({
      next: (user) => {
        this.currentUser = user
      },
      error: () => {
        this.router.navigate(['/user/login'])
      }
    })
  }

  enterEditMode(): void {
    this.isInEditMode = true;

    setTimeout(() => {
      this.editProfileForm.form.patchValue({
        firstName: this.currentUser.first_name,
        lastName: this.currentUser.last_name,
        age: this.currentUser.age,
        profileImage: this.currentUser.profile_image,
        socialFacebook: this.currentUser.facebook_url,
        socialLinkedIn: this.currentUser.linked_in_url,
        socialGitHub: this.currentUser.github_url,
      })
    });
  }

  updateProfile(): void {
    this.isInEditMode = false;
  }

}
