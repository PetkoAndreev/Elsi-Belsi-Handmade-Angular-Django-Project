import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpResponse
} from '@angular/common/http';
import { Observable, tap } from 'rxjs';
import { IUser } from '../interfaces';
import { AuthService } from '../services/auth.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(
    private authService: AuthService,
  ) { }

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    return next.handle(request).pipe(tap(event => {
      if (event instanceof HttpResponse) {
        // localhost:8000/api/auth/login || localhost:8000/api/auth/register || event.url?.endsWith('register/')
        if (event.url?.endsWith('login/') ) {
          const newlyLoggedInUser: IUser = event.body as IUser;
          // Saves newly logged in user in the auth service
          this.authService.handleLogin(newlyLoggedInUser);
        }
        else if (event.url?.endsWith('logout/')) {
          this.authService.handleLogout()
        }
      }
    }));
  }
}
