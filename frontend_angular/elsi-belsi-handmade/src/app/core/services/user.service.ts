import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, tap } from 'rxjs';
import { environment } from 'src/environments/environment';
import { IProfile, IUser } from '../interfaces';

export interface CreateUserDto { email: string, password: string, confirm_password: string }

@Injectable()
export class UserService {

  currentUser!: IUser;
  currentProfile!: IProfile;

  get isLoggedIn() {
    return !!this.currentUser;
  }

  constructor(
    private httpClient: HttpClient,
  ) { }

  login$(userData: { email: string, password: string }): Observable<IUser> {
    return this.httpClient
      .post<IUser>(`${environment.apiUrl}/auth/login/`, userData, { withCredentials: true })
      .pipe(tap(user => this.currentUser = user))
  }

  logout(): void {
  }

  register$(userData: CreateUserDto): Observable<IUser> {
    return this.httpClient.post<IUser>(`${environment.apiUrl}/auth/register/`, userData, { withCredentials: true });
  }

  getProfile$(id: number): Observable<IProfile> {
    return this.httpClient.get<IProfile>(`${environment.apiUrl}/auth/profile/${id}/`, { withCredentials: true }).pipe(tap(user => this.currentProfile = user));
  }
}
