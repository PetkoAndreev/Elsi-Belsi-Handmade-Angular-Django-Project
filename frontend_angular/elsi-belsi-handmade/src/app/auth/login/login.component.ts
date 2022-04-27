import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UserService } from 'src/app/core/services/user.service';
import { emailPattern, passwordPattern } from '../auth-utils';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  errorMessage: string = '';

  loginFormGroup: FormGroup = this.formBuilder.group({
    'email': new FormControl('', [Validators.required, Validators.pattern(emailPattern),]),
    'password': new FormControl('', [Validators.required, Validators.pattern(passwordPattern),])
  });

  constructor(
    private userService: UserService,
    private router: Router,
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
  }

  shouldShowControlError(controlName: string, sourceGroup: FormGroup = this.loginFormGroup) {
    return sourceGroup.controls[controlName].touched && sourceGroup.controls[controlName].invalid
  }

  shouldShowControlClass(controlName: string, sourceGroup: FormGroup = this.loginFormGroup) {
    return sourceGroup.controls[controlName].touched && !sourceGroup.controls[controlName].invalid
  }

  shouldShowValidatorError(controlName: string, validatorName: string = 'required') {
    return this.loginFormGroup.controls[controlName].errors?.[validatorName]
  }

  handleLogin(): void {
    this.errorMessage = '';
    this.userService.login$(this.loginFormGroup.value).subscribe({
      next: () => {
        this.router.navigate(['/home']);
      },
      complete: () => {

      },
      error: (err) => {
        console.log(err)
        this.errorMessage = err.error.message
      }
    })
  }

}
