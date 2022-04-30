import { IProfile, IUser } from '../interfaces';

export * from './actions';
export * from './reducers';

export interface IRootState {
    currentUser: IUser;
}