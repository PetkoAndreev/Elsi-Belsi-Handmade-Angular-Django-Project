import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/core/services/auth.service';
import { CreateUserDto } from 'src/app/core/services/user.service';
import { emailPattern, passwordMatch, passwordPattern } from '../auth-utils';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  get passwordsGroup(): FormGroup {
    return this.registerFormGroup.controls['passwords'] as FormGroup;
  };
  passwordControl = new FormControl(null, [Validators.required, Validators.pattern(passwordPattern),]);

  errorMessage: string = '';

  registerFormGroup: FormGroup = this.formBuilder.group({
    email: new FormControl(null, [Validators.required, Validators.pattern(emailPattern),]),
    passwords: new FormGroup({
      password: this.passwordControl,
      rePassword: new FormControl(null, [passwordMatch(this.passwordControl),])
    })
  });

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router,
  ) { }

  ngOnInit(): void {
  }

  shouldShowControlError(controlName: string, sourceGroup: FormGroup = this.registerFormGroup) {
    return sourceGroup.controls[controlName].touched && sourceGroup.controls[controlName].invalid
  }

  shouldShowControlClass(controlName: string, sourceGroup: FormGroup = this.registerFormGroup) {
    return sourceGroup.controls[controlName].touched && !sourceGroup.controls[controlName].invalid
  }

  shouldShowValidatorError(controlName: string, validatorName: string = 'required', sourceGroup: FormGroup = this.registerFormGroup) {
    return sourceGroup.controls[controlName].errors?.[validatorName]
  }

  handleRegister(): void {
    this.errorMessage = '';
    const { email, passwords } = this.registerFormGroup.value;

    const body: CreateUserDto = {
      email: email,
      password: passwords.password,
      confirm_password: passwords.rePassword,
    }

    this.authService.register$(body).subscribe({
      next: () => {
        this.router.navigate(['/user/login']);
      },
      complete: () => {

      },
      error: (err) => {
        this.errorMessage = 'Someone with that email address has already registered. Was it you?'
      }
    })
  }

}
