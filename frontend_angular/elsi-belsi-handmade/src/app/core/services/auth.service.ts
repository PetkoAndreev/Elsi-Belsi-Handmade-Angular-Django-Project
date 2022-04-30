import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Store } from '@ngrx/store';
import { BehaviorSubject, catchError, EMPTY, map, Observable, tap } from 'rxjs';
import { environment } from 'src/environments/environment';
import { IProfile, IUser } from '../interfaces';
import { IRootState, login, logout } from '../ngrx';
import { CreateUserDto } from './user.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  // Handle the logic for registration, login and authentication

  private _currentUser = new BehaviorSubject<IUser>(undefined!);

  // currentUser$ = this._currentUser.asObservable();
  // Get current user from the global state
  currentUser$ = this.store.select(globalState => globalState.currentUser);
  isLoggedIn$: Observable<boolean> = this.currentUser$.pipe(map(user => !!user))

  constructor(
    private httpClient: HttpClient,
    private store: Store<IRootState>,
  ) { }

  login$(userData: { email: string, password: string }): Observable<IUser> {
    return this.httpClient
      .post<IUser>(`${environment.apiUrl}/auth/login/`, userData, { withCredentials: true, observe: 'response', })
      .pipe(
        map((response: { body: any; }) => {
          localStorage.setItem('access_token', response.body.data.access)
          localStorage.setItem('refresh_token', response.body.data['refresh'])
          return response.body;
        }),
        map((response: { body: any; }) => response.body),
      )
  }

  logout$(): Observable<void> {
    return this.httpClient
      .post<void>(`${environment.apiUrl}/auth/logout/`, { withCredentials: true, })
  }

  register$(userData: CreateUserDto): Observable<IUser> {
    return this.httpClient.post<IUser>(`${environment.apiUrl}/auth/register/`, userData, { withCredentials: true });
  }

  handleLogin(newUser: IUser) {
    // NGRX Login
    this.store.dispatch(login({ user: newUser }));
    this._currentUser.next(newUser);
    console.log(this.currentUser$);
  }

  handleLogout() {
    // NGRX Logout
    this.store.dispatch(logout());
    // this._currentUser.next(undefined!);
  }

  authenticate(): Observable<IUser> {
    return this.httpClient
      .get<IUser>(`${environment.apiUrl}/auth/profile/`, { withCredentials: true })
      .pipe(tap(currentProfile => this.handleLogin(currentProfile)), catchError((err) => {
        return EMPTY;
      }))
  }
}
