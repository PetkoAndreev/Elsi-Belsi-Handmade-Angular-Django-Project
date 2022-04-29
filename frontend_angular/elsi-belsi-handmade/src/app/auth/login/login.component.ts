import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from 'src/app/core/services/auth.service';
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
    private authService: AuthService,
    private router: Router,
    private formBuilder: FormBuilder,
    private activatedRoute: ActivatedRoute,
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
    this.authService.login$(this.loginFormGroup.value).subscribe({
      next: () => {
        // Navigation to the page before login, e.g. if we try to add new product, but we're not logged in - after this it'll navigate us to the add new product page insted of home page.
        if (this.activatedRoute.snapshot.queryParams['redirect-to']) {
          this.router.navigateByUrl(this.activatedRoute.snapshot.queryParams['redirect-to'])
        }
        else {
          this.router.navigate(['/home']);
        }
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
